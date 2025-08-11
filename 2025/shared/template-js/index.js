// Import AOC Common
const fs = require('fs');
const path = require('path');
// const aocCommon = require('../shared/aoc_common');
// const aocAlgorithms = require('../shared/aoc_algorithms');


const P1_DEBUG = true;
const P2_DEBUG = true;

const USE_REAL_DATA = false; // Loads input.txt when true or sample.txt when false

const INPUT_FILENAME = `${path.dirname(__filename)}/input.txt`;
const SAMPLE_FILENAME = `${path.dirname(__filename)}/sample.txt`;

function part1(input) {
    if (P1_DEBUG) console.log("Doing Part 1 things");
    return "part 1 answer";
}

function part2(input) {
    if (P2_DEBUG) console.log("Doing Part 2 things");
    return "part 2 answer";
}

if (require.main === module) {
    const parsedInput = aocCommon.importFileSingleNewLine(USE_REAL_DATA ? INPUT_FILENAME : SAMPLE_FILENAME);

    const startTimePart1 = Date.now();
    const part1Result = part1(parsedInput);
    const endTimePart1 = Date.now();

    const startTimePart2 = Date.now();
    const part2Result = part2(parsedInput);
    const endTimePart2 = Date.now();

    console.log("# # # SOLUTIONS # # #");
    console.log(`Part 1: ${part1Result} \t ⏱️ in ${(endTimePart1 - startTimePart1) / 1000} seconds`);
    console.log(`Part 2: ${part2Result} \t ⏱️ in ${(endTimePart2 - startTimePart2) / 1000} seconds`);
}
