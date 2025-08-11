const fs = require('fs');
const path = require('path');

const COOKIE_CACHE = path.resolve(__dirname, '../../COOKIE');


const importFileSingleNewLine = (inputFilename) => {
    return fs.readFileSync(inputFilename, 'utf-8')
        .split('\n')
        .filter(line => line.trim());
};

const importFileDoubleNewLine = (inputFilename) => {
    return fs.readFileSync(inputFilename, 'utf-8')
        .split('\n\n')
        .filter(line => line.trim());
};

const importFileAsGrid = (inputFilename) => {
    const input = fs.readFileSync(inputFilename, 'utf-8')
        .split('\n')
        .filter(line => line.trim());

    return input.map(line => [...line]);
};

const product = (lst) => {
    return lst.map(Number).reduce((acc, val) => acc * val, 1);
};

const threePartParseDict = (input, firstDelim, secondDelim) => {
    const output = {};

    input.forEach(line => {
        const [partA, tmp] = line.split(firstDelim);
        const [partB, partC] = tmp.split(secondDelim);
        output[partA] = [partB.split(), partC.split()];
    });

    return output;
};

const importTwoPartInput = (input, firstPartDelim = ',', secondPartDelim = ',') => {
    const [part1, part2] = importFileDoubleNewLine(input);

    return [
        part1.split('\n').map(x => x.split(firstPartDelim)),
        part2.split('\n').map(x => x.split(secondPartDelim))
    ];
};

const convertListOfListsToInts = (list) => {
    return list.map(sublist => sublist.map(item => parseInt(item, 10)));
};

const drawGridToConsole = (grid, delay = 100, clear = true) => {
    if (clear) {
        console.clear();
    }

    grid.forEach(row => {
        console.log(row.join(''));
    });

    setTimeout(() => {}, delay);
};

const isInBoundsOfGrid = (grid, [row, col]) => {
    return row >= 0 && row < grid.length && col >= 0 && col[0].length;
};

const findCoordsOfCharInGrid = (grid, char) => {
    const coords = [];

    grid.forEach((row, rowIndex) => {
        row.forEach((cell, colIndex) => {
            if (cell === char) {
                coords.push([rowIndex, colIndex]);
            }
        });
    });

    return coords;
};

module.exports = {
    importFileSingleNewLine,
    importFileDoubleNewLine,
    importFileAsGrid,
    product,
    threePartParseDict,
    importTwoPartInput,
    convertListOfListsToInts,
    drawGridToConsole,
    isInBoundsOfGrid,
    findCoordsOfCharInGrid
};
