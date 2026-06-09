package main

import (
	"bufio"
	"os"
	"strings"
)

// TODO: Add helper functions here as you learn Go
// Placeholder functions ready for implementation:

// importFileSingleNewLine reads a file and returns a slice of strings split by newlines
func importFileSingleNewLine(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line != "" {
			lines = append(lines, line)
		}
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return lines, nil
}

// TODO: Add more helper functions below as needed
// Examples for future implementation:
// - parseIntSlice(line string, sep string) []int
// - parseStringSlice(line string, sep string) []string
// - loadGridFromFile(filename string) [][]rune
// - etc.
