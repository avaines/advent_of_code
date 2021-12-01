const filepath = "./input.txt"

function readTextSync(filename){
  fs = require('fs');
  return fs.readFileSync(filename).toString().split("\n");
}

function day1(inputList){
    let numOfIncreases = 0
    let previousValue = parseInt(inputList[0])

    for (let i=1; i < inputList.length; i++) {
        let currentValue = parseInt(inputList[i])

        if (currentValue > previousValue) {
            // console.log(`%i is greater than %i`,currentValue, previousValue )
            numOfIncreases ++
        } else {
            // console.log(`%i is less than %i`,currentValue, previousValue )
        }
        
        // Move on to the next one
        previousValue = currentValue
        
    }
    return numOfIncreases
}


function day2(inputList){
    let newList = []

    for (let i=0; i < inputList.length -2 ; i++) {
        let m1 = parseInt(inputList[i])
        let m2 = parseInt(inputList[i+1])
        let m3 = parseInt(inputList[i+2])

        newList.push(m1+m2+m3)
        
    }

    return newList
}


let myList = readTextSync(filepath, true)
let day1Answer = day1(myList)
let day2List = day2(myList)
let day2Answer = day1(day2List)

console.log("Day1: " + day1Answer )
console.log("Day2: " + day2Answer )



// ToDo for tomorrow:
// Load a list of numbers, not string
// conditional output messages
// central shared functions