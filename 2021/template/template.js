const filepath = "./input.txt"
const aocHelpers = require("../shared/functions");
// const aocClasses = require("../shared/submarine");


function part1(inputList, DEBUG){
    DEBUG && console.log("part1")
    return 0
}


function part2(inputList, DEBUG){
    DEBUG && console.log("part2")
    return 0
}


let myInput = aocHelpers.readTextToListInt(filepath)
let part1Answer = part1(myInput, true)
let part2Answer = part2(myInput, false)


console.log("==========================")
console.log("| Part 1 : " + part1Answer )
console.log("| Part 2 : " + part2Answer )
