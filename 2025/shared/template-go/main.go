package main

import (
	"fmt"
	"os"
	"path/filepath"
	"time"
)

const (
	P1_DEBUG      = true
	P2_DEBUG      = true
	USE_REAL_DATA = false // Use input.txt when true, sample.txt when false
)

func part1(input []string) string {
	if P1_DEBUG {
		fmt.Println("Doing Part 1 things")
	}
	return "part 1 answer"
}

func part2(input []string) string {
	if P2_DEBUG {
		fmt.Println("Doing Part 2 things")
	}
	return "part 2 answer"
}

func main() {
	// Determine which file to use
	filename := "sample.txt"
	if USE_REAL_DATA {
		filename = "input.txt"
	}

	// Get the directory of the current file
	ex, err := os.Executable()
	if err != nil {
		panic(err)
	}
	exePath := filepath.Dir(ex)
	filePath := filepath.Join(exePath, filename)

	// Parse input
	parsedInput, err := importFileSingleNewLine(filePath)
	if err != nil {
		panic(err)
	}

	// Part 1
	startTimePart1 := time.Now()
	part1Result := part1(parsedInput)
	endTimePart1 := time.Now()

	// Part 2
	startTimePart2 := time.Now()
	part2Result := part2(parsedInput)
	endTimePart2 := time.Now()

	// Output results
	fmt.Println("# # # SOLUTIONS # # #")
	fmt.Printf("Part 1: %s \t ⏱️  in %.4f seconds\n", part1Result, endTimePart1.Sub(startTimePart1).Seconds())
	fmt.Printf("Part 2: %s \t ⏱️  in %.4f seconds\n", part2Result, endTimePart2.Sub(startTimePart2).Seconds())
}
