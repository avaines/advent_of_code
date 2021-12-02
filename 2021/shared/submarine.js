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

module.exports = { Submarine: Submarine }