import os
import argparse
import shutil
import requests
from bs4 import BeautifulSoup


COOKIE_CACHE = "./COOKIE"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AoC Helper Script")
    parser.add_argument("--year", "-y", type=int, help="Year of the AoC")
    parser.add_argument("--day", "-d", type=int, help="Day in December for the AoC")
    parser.add_argument("--session", "-s", type=str, help="Session cookie for AoC website")

    args = parser.parse_args()

    year_dir = f"./{args.year}"
    day_dir = f"{year_dir}/{args.day}"

    # Check if year exists
    if not os.path.exists(year_dir):
        print(f"Year directory {year_dir} does not exist. Creating.")
        os.makedirs(year_dir)

    # Check or prompt for session cookie
    session_cookie = args.session
    if not session_cookie:
        if os.path.exists(COOKIE_CACHE):
            with open(COOKIE_CACHE, "r") as cache_file:
                session_cookie = cache_file.read().strip()
                print("Using cached session cookie.")
        else:
            session_cookie = input("Enter AoC session cookie: ")
            with open(COOKIE_CACHE, "w") as cache_file:
                cache_file.write(session_cookie)
                print("Session cookie cached.")

    # Connect to the AoC API to get puzzle details
    puzzle_url = f"https://adventofcode.com/{args.year}/day/{args.day}"
    headers = {"Cookie": f"session={session_cookie}"}

    response = requests.get(puzzle_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch puzzle details. HTTP Status: {response.status_code}")
        exit()

    # Extract puzzle title
    try:
        soup = BeautifulSoup(response.text, "html.parser")
        puzzle_title = soup.find("h2").text.strip()
    except Exception as e:
        print(f"Error extracting puzzle title: {e}")
        exit()

    puzzle_title_slug = puzzle_title.strip("--- ").strip(" ---").replace(":","").strip()
    puzzle_dir = f"{year_dir}/{puzzle_title_slug}"

    # Check if day exists
    if os.path.exists(puzzle_dir):
        print(f"Directory for day {puzzle_dir} already exists. Exiting")
        exit()

    # Copy template directory to puzzle directory
    template_dir = f"{year_dir}/template"
    if not os.path.exists(template_dir):
        print(f"Template directory {template_dir} does not exist. Exiting.")
        exit()

    shutil.copytree(template_dir, puzzle_dir)
    print(f"Copied template to {puzzle_dir}")

    # Download puzzle input
    input_url = f"{puzzle_url}/input"
    input_response = requests.get(input_url, headers=headers)
    if input_response.status_code != 200:
        print(f"Failed to fetch puzzle input. HTTP Status: {input_response.status_code}")
        exit()

    input_path = os.path.join(puzzle_dir, "input.txt")
    with open(input_path, "w") as input_file:
        input_file.write(input_response.text)
        print("Puzzle input saved:")

    print(f"Puzzle directory generated in:")
    print(puzzle_dir)
