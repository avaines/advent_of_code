const aocHelpers = require("./functions");
class Submarine {
    constructor(depth, position, aim, DEBUG) {
        this.depth = depth
        this.position = position
        this.aim = aim
        this.DEBUG = DEBUG

        this.powerConsumption = 0
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
        let gammaRate = "" // most common (Mode) bit in each position
        let epsilonRate = "" // least common (anti-mode?) bit in each position

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
    }

}

module.exports = { Submarine }