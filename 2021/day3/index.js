const filepath = "./input.txt"
const aocHelpers = require("../shared/functions");
const aocClasses = require("../shared/submarine");


function part2(inputList, DEBUG){

      // Diagnostic report
      let oxygenRating = "" // most common (Mode) bit in each position
      let co2ScrubberRating = "" // least common (anti-mode?) bit in each position
      

      // Oxygen
      let filteredList = inputList

      // For each position/column in the data, and while there are more than 1 entries in the list
      let curIndex = 0
      while(filteredList.length > 1) {
        
        // make an array from the vaules in this column
        // create a map (for loop) of the filtered list and for each entry in it
        let curColumn = filteredList.map((entry) => entry[curIndex])

        // with this new array find the mode value of it
        let mostFrequentValue = aocHelpers.getFrequent(curColumn).pop()
        
        DEBUG && console.log(filteredList)
        DEBUG && console.log(`Most frequest value at position %i, is %s`, curIndex+1, mostFrequentValue )

        // Filter the list of elements WITH the mostFrequentValue value in the current column/position
        let newFilteredList=[]
        for (i=0; i < filteredList.length; i++) {
          if (filteredList[i][curIndex] == mostFrequentValue){
            newFilteredList.push(filteredList[i])
          }
        }

        filteredList = newFilteredList
        curIndex++
      }

      oxygenRating = parseInt(filteredList[0],2)


      // CO2
      filteredList = inputList

      // For each position/column in the data, and while there are more than 1 entries in the list
      curIndex = 0
      while(filteredList.length > 1) {
        
        // make an array from the vaules in this column
        // create a map (for loop) of the filtered list and for each entry in it
        let curColumn = filteredList.map((entry) => entry[curIndex])

        // with this new array find the mode value of it
        let leastsFrequentValue = aocHelpers.getFrequent(curColumn, true).shift()
        
        DEBUG && console.log(filteredList)
        DEBUG && console.log(`Most frequest value at position %i, is %s`, curIndex+1, leastsFrequentValue )

        // Filter the list of elements WITH the leastsFrequentValue value in the current column/position
        let newFilteredList=[]
        for (i=0; i < filteredList.length; i++) {
          if (filteredList[i][curIndex] == leastsFrequentValue){
            newFilteredList.push(filteredList[i])
          }
        }

        filteredList = newFilteredList
        curIndex++
      }

      co2ScrubberRating = parseInt(filteredList[0],2)

    let lifeSupportRating = oxygenRating * co2ScrubberRating
    return lifeSupportRating
    
}

let myInput = aocHelpers.readTextToList(filepath)
let submarine = new aocClasses.Submarine(0, 0, 0, true)

// Part 1 Function, moved into the Submarine
submarine.diagnostics(myInput)

// Part 2 Function
let part2Answer = part2(myInput, true)

console.log("==========================")
console.log("| Part 1 : " + submarine.powerConsumption ) //3242606
console.log("| Part 2 : " + part2Answer ) //4856080
