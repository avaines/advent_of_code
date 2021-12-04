const aocHelpers = require("./functions");
class Submarine {
    constructor(depth, position, aim, DEBUG) {
        this.depth = depth
        this.position = position
        this.aim = aim
        this.DEBUG = DEBUG

        this.powerConsumption = 0
        this.lifeSupportRating = 0
    }

    status() {
        return (this.depth, this.position)
    }

    move(instruction){
        let [direction, units] = instruction.split(' ')
        units = parseInt(units) // Convert string to int for the units

        switch(direction) {
            case 'forward':
                this.position += units
                this.depth += this.aim * units
                break;
            case 'up':
                this.aim -= units
                break;
            case 'down':
                this.aim += units
                break;
        }

        if (this.DEBUG && ['forward', 'backward'].includes(direction) ) {
            console.log(`%s %i changes by %i to your horizontal position, a total of %i`, direction, units, units, this.position)
            console.log(`   Your aim is %i, resulting in a depth of %i`, this.aim, this.depth)
        } else {
            console.log(`%s %i changes by %i to your aim, a total of %i`, direction, units, units, this.aim)
        }

    }

    diagnostics(report){
        let gammaRate = "" // MOST common bit in each position 
        let epsilonRate = "" // LEAST common bit in each position
        let oxygenRating = "" // Entry with each bit in each position being MOST common
        let co2ScrubberRating = "" // Entry with each bit in each position being LEAST common
        
        //  Gamma and Epsilon Rates
        for (let i=0; i < report[0].length; i++) {

            // Using a map 'vertically select' the nth column and workout the most/least common value
            let x = report.map((entry) => entry[i])

            // Gamma rate is assembled from the MOST common bit in the current column
            gammaRate += aocHelpers.getFrequent(x).pop()
            
            // Epsilon rate is assembled from the LEAST common bit in the current column
            epsilonRate += aocHelpers.getFrequent(x,true).shift()
            
        }
        this.DEBUG && console.log(`GammaRate: %s (%i)  |  EpsilonRate: %s (%i)`, gammaRate, parseInt(gammaRate,2), epsilonRate, parseInt(epsilonRate,2))
        this.powerConsumption = parseInt(gammaRate,2) * parseInt(epsilonRate,2)

        
      // Oxygen Rating
      let filteredList = report

      // For each position/column in the data, and while there are more than 1 entries in the list
      let curIndex = 0
      while(filteredList.length > 1) {
        
        // make an array from the vaules in this column
        // create a map (for loop) of the filtered list and for each entry in it
        let curColumn = filteredList.map((entry) => entry[curIndex])

        // with this new array find the mode value of it
        let mostFrequentValue = aocHelpers.getFrequent(curColumn).pop()
        
        this.DEBUG && console.log(filteredList)
        this.DEBUG && console.log(`Most frequest value at position %i, is %s`, curIndex+1, mostFrequentValue )

        // Filter the list of elements WITH the mostFrequentValue value in the current column/position
        let newFilteredList=[]
        for (let i=0; i < filteredList.length; i++) {
          if (filteredList[i][curIndex] == mostFrequentValue){
            newFilteredList.push(filteredList[i])
          }
        }

        filteredList = newFilteredList
        curIndex++
      }

      oxygenRating = parseInt(filteredList[0],2)


      // CO2 Rating
      filteredList = report  // Reset the filtered lists 'view'

      // For each position/column in the data, and while there are more than 1 entries in the list
      curIndex = 0
      while(filteredList.length > 1) {
        
        // make an array from the vaules in this column
        // create a map (for loop) of the filtered list and for each entry in it
        let curColumn = filteredList.map((entry) => entry[curIndex])

        // with this new array find the mode value of it
        let leastFrequentValue = aocHelpers.getFrequent(curColumn, true).shift()
        
        this.DEBUG && console.log(filteredList)
        this.DEBUG && console.log(`Most frequest value at position %i, is %s`, curIndex+1, leastFrequentValue )

        // Filter the list of elements WITH the leastFrequentValue value in the current column/position
        let newFilteredList=[]
        for (let i=0; i < filteredList.length; i++) {
          if (filteredList[i][curIndex] == leastFrequentValue){
            newFilteredList.push(filteredList[i])
          }
        }

        filteredList = newFilteredList
        curIndex++
      }

      co2ScrubberRating = parseInt(filteredList[0],2)

      this.lifeSupportRating = oxygenRating * co2ScrubberRating

    }

}

module.exports = { Submarine }