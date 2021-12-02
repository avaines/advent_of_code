const filepath = "./input.txt"
const aocHelpers = require("../shared/functions");

function part1(inputList, DEBUG){
    let numOfIncreases = 0
    let previousValue = inputList[0]

    for (let i=1; i < inputList.length; i++) {
        let currentValue = inputList[i]

        if (currentValue > previousValue) {
            DEBUG && console.log(`%i is greater than %i`,currentValue, previousValue )
            numOfIncreases ++
        } else {
            DEBUG && console.log(`%i is less than %i`,currentValue, previousValue )
        }

        previousValue = currentValue
    }
    return numOfIncreases
}


function part2(inputList, DEBUG){
    let newList = []

    for (let i=0; i < inputList.length -2 ; i++) {
        let m1 = inputList[i]
        let m2 = inputList[i+1]
        let m3 = inputList[i+2]

        newList.push(m1+m2+m3)
    }
    return newList
}

let myInput = aocHelpers.readTextToListInt(filepath)
let part1Answer = part1(myInput, false)
let part2List = part2(myInput, false)
let part2Answer = part1(part2List, false)

console.log("part1: " + part1Answer )
console.log("part2: " + part2Answer )
