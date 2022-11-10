const filepath = "./sample.txt"
const aocHelpers = require("../shared/functions");
// const aocClasses = require("../shared/submarine");

function part1(inputList, DEBUG){ 
    const numbers = inputList[0].split(',').map(Number)
    const cards = []
    let foundWinner = false
    let sumOfAllUnMarkedNumbers = 0
    let lastCalledNumber = 0
    
    for (let i = 2; i < inputList.length - 4; i += 6) {
        const card = {
            values: [],
            checked: Array(5).fill().map(() => Array(5).fill(0))
        };

        for (let j = 0; j < 5; j++) {
            card.values.push(inputList[i + j].split(' ').filter(num => num != '').map(Number));
        }
        
        cards.push(card);
    }

    const hasBingo = card => {
        let bingo = false;
        // check if rows have bingo
        card.checked.forEach(row => {
            if (row.reduce((old, curr) => old + curr, 0) == 5) {
                bingo = true;
            }
        })
        // check if columns have bingo
        for (let i = 0; i < 5; i++) {
            let sumOnColumn = 0;
            for (let j = 0; j < 5; j++) {
                sumOnColumn += card.checked[j][i];
            }
            if (sumOnColumn >= 5) {
                bingo = true;
            }
        }
        return bingo;
    };

    const tickNumOnCard = (card, num) => {
        for (let i = 0; i < 5; i++) {
            for (let j = 0; j < 5; j++) {
                if (card.values[i][j] == num) {
                    card.checked[i][j] = 1;
                }
            }
        }
    };

    const getScore = (card) => {
        let sumValuesOnCard = 0;
        for (let i = 0; i < 5; i++) {
            for (let j = 0; j < 5; j++) {
                if (card.checked[i][j] == 0) {
                    sumValuesOnCard += card.values[i][j];
                }
            }
        }
        return sumValuesOnCard;
    };

    numbers.some(num => {
        cards.some(card => {
            tickNumOnCard(card, num);

            if (hasBingo(card)) {
                sumOfAllUnMarkedNumbers = getScore(card)
                lastCalledNumber = num
                foundWinner = true;
            }
            return foundWinner;
        })
        return foundWinner;
    });

    return sumOfAllUnMarkedNumbers * lastCalledNumber
    
}


function part2(inputList, DEBUG){
    DEBUG && console.log("part2")
    return 0
}


// let myInput = aocHelpers.readTextToListInt(filepath)
let myInput = aocHelpers.readTextToList(filepath)

let part1Answer = part1(myInput, true)
let part2Answer = part2(myInput, false)


console.log("==========================")
console.log("| Part 1 : " + part1Answer )
console.log("| Part 2 : " + part2Answer )




// const input = fs.readFileSync('sample.txt', 'utf8').split('\n');


