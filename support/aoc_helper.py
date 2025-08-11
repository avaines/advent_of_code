"""
AoC Helper Script

This script automates the setup process for Advent of Code puzzles. It performs the following tasks:
1. Creates a directory structure for the specified year and day.
2. Retrieves the session cookie for authentication, either from a cache or user input.
3. Fetches puzzle details and input from the Advent of Code website.
4. Copies a language-specific template to the puzzle directory.
5. Saves the puzzle input to a file.

Usage:
    python aoc_helper.py --year <YEAR> --day <DAY> [--session <SESSION_COOKIE>] [--language <LANGUAGE>]

Arguments:
    --year, -y       The year of the Advent of Code event.
    --day, -d        The day of the puzzle in December.
    --session, -s    The session cookie for authentication (optional).
    --language, -l   The programming language for the solution (default: python).
"""

import os
import argparse
import sys
import shutil
import requests
from bs4 import BeautifulSoup


COOKIE_CACHE = "./COOKIE"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AoC Helper Script")
    parser.add_argument("--year", "-y", type=int, help="Year of the AoC")
    parser.add_argument("--day", "-d", type=int, help="Day in December for the AoC")
    parser.add_argument("--session", "-s", type=str, help="Session cookie for AoC website")
    parser.add_argument("--language", "-l", type=str, help="Programming language for the solution",
                        default="python")

    args = parser.parse_args()

    YEAR_DIR = f"./{args.year}"
    DAY_DIR = f"{YEAR_DIR}/{args.day}"

    # Check if year exists
    if not os.path.exists(YEAR_DIR):
        print(f"Year directory {YEAR_DIR} does not exist. Creating.")
        os.makedirs(YEAR_DIR)

    # Check or prompt for session cookie
    session_cookie = args.session
    if not session_cookie:
        if os.path.exists(COOKIE_CACHE):
            with open(COOKIE_CACHE, "r", encoding="utf-8") as cache_file:
                session_cookie = cache_file.read().strip()
                print("Using cached session cookie.")
        else:
            session_cookie = input("Enter AoC session cookie: ")
            with open(COOKIE_CACHE, "w", encoding="utf-8") as cache_file:
                cache_file.write(session_cookie)
                print("Session cookie cached.")

    # Connect to the AoC API to get puzzle details
    PUZZLE_URL = f"https://adventofcode.com/{args.year}/day/{args.day}"
    headers = {"Cookie": f"session={session_cookie}"}

    response = requests.get(PUZZLE_URL, headers=headers, timeout=10)
    if response.status_code != 200:
        print(f"Failed to fetch puzzle details. HTTP Status: {response.status_code}")
        exit()

    # Extract puzzle title
    try:
        soup = BeautifulSoup(response.text, "html.parser")
        puzzle_title = soup.find("h2").text.strip()
    except AttributeError as e:
        print(f"Error extracting puzzle title: {e}")
        sys.exit()

    puzzle_title_slug = puzzle_title.strip("--- ").strip(" ---").replace(":","").strip()
    PUZZLE_DIR = f"{YEAR_DIR}/{puzzle_title_slug}"

    # Check if day exists
    if os.path.exists(PUZZLE_DIR):
        print(f"Directory for day {PUZZLE_DIR} already exists. Exiting")
        sys.exit()

    # Copy template directory to puzzle directory
    match args.language:
        case "python":
            TEMPLATE_DIR = f"{YEAR_DIR}/shared/template-py"
        case "js":
            TEMPLATE_DIR = f"{YEAR_DIR}/shared/template-js"
        case _:
            TEMPLATE_DIR = f"{YEAR_DIR}/shared/template-py"

    if not os.path.exists(TEMPLATE_DIR):
        print(f"Template directory {TEMPLATE_DIR} does not exist. Exiting.")
        sys.exit()

    shutil.copytree(TEMPLATE_DIR, PUZZLE_DIR)
    print(f"Copied {args.language} template to {PUZZLE_DIR}")

    # Download puzzle input
    INPUT_URL = f"{PUZZLE_URL}/input"
    input_response = requests.get(INPUT_URL, headers=headers, timeout=10)
    if input_response.status_code != 200:
        print(f"Failed to fetch puzzle input. HTTP Status: {input_response.status_code}")
        exit()

    input_path = os.path.join(PUZZLE_DIR, "input.txt")
    with open(input_path, "w", encoding="utf-8") as input_file:
        input_file.write(input_response.text)
        print("Puzzle input saved:")

    print(f"Puzzle directory generated in:{PUZZLE_DIR}")
