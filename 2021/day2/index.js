const filepath = "./input.txt"
const aocHelpers = require("../shared/functions");
const aocClasses = require("../shared/submarine");

let submarine = new aocClasses.Submarine(0, 0, 0, true)
let myInput = aocHelpers.readTextToList(filepath)

for (let i=0; i < myInput.length; i++) {
    submarine.move(myInput[i])
}

console.log("==========================")
console.log("| Part 1 : 1990000") // Part2 invalidates the submarine class functions for part 1
console.log(`| Part 2 : The Submarine has a position of %i and a depth of %i with a final position of %i`, submarine.position, submarine.depth, submarine.position * submarine.depth )
