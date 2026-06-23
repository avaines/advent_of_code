package main

import (
	"aocshared"
	"fmt"
	"os"
	"path/filepath"
	"time"
)

const (
	P1_DEBUG      = true
	P2_DEBUG      = true
	USE_REAL_DATA = true // Use input.txt when true, sample.txt when false
)

func part1(input []string) string {
	targetFloor := 0

	for _, char := range input[0] {
		switch char {
		case '(':
			if P1_DEBUG {
				fmt.Println("Going UP 1 floor")
			}
			targetFloor++
		case ')':
			if P1_DEBUG {
				fmt.Println("Going DOWN 1 floor")
			}
			targetFloor--
		}
	}

	return fmt.Sprintf("%d", targetFloor)
}

func part2(input []string) string {
	targetFloor := 0

	for i, char := range input[0] {
		switch char {
		case '(':
			if P2_DEBUG {
				fmt.Println("Going UP 1 floor")
			}
			targetFloor++
		case ')':
			if P2_DEBUG {
				fmt.Println("Going DOWN 1 floor")
			}
			targetFloor--
		}

		if targetFloor == -1 {
			if P2_DEBUG {
				fmt.Println("Entering Basement...")
			}
			return fmt.Sprintf("%d", i+1)
		}
	}

	return "-1"
}

func main() {
	// Determine which file to use
	filename := "sample.txt"
	if USE_REAL_DATA {
		filename = "input.txt"
	}

	// Resolve input from the current directory first (works with go run),
	// then fall back to the executable directory.
	workingDir, err := os.Getwd()
	if err != nil {
		panic(err)
	}
	filePath := filepath.Join(workingDir, filename)
	if _, err := os.Stat(filePath); err != nil {
		ex, err := os.Executable()
		if err != nil {
			panic(err)
		}
		exePath := filepath.Dir(ex)
		filePath = filepath.Join(exePath, filename)
	}

	// Parse input
	parsedInput, err := aocshared.ImportFileSingleNewLine(filePath)
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
