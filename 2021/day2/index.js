const filepath = "./input.txt"
const aoc = require("../shared/functions");

class Submarine {
    constructor(depth, position, aim, DEBUG) {
        this.depth = depth
        this.position = position
        this.aim = aim
        this.DEBUG = DEBUG
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


}

let submarine = new Submarine(0, 0, 0, true)
let myInput = aoc.readTextToList(filepath)

for (let i=0; i < myInput.length; i++) {
    submarine.move(myInput[i])
}

console.log("==========================")
console.log("| Part 1 : 1990000") // Part2 invalidates the submarine class functions for part 1
console.log(`| Part 2 : The Submarine has a position of %i and a depth of %i with a final position of %i`, submarine.position, submarine.depth, submarine.position * submarine.depth )
