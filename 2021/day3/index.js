const filepath = "./input.txt"
const aocHelpers = require("../shared/functions");
const aocClasses = require("../shared/submarine");

let myInput = aocHelpers.readTextToList(filepath)
let submarine = new aocClasses.Submarine(0, 0, 0)

// Part 1 & 2 Function, moved into the Submarine
submarine.diagnostics(myInput)

console.log("==========================")
console.log("| Part 1 : " + submarine.powerConsumption ) //3242606
console.log("| Part 2 : " + submarine.lifeSupportRating ) //4856080
