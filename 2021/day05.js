const fs = require('fs')
const path = require('path')

function readInput(filename) {
    return fs.readFileSync(path.join('inputs', filename), 'utf8')
}

function isVertical(line) {
    return line[0][0] == line[1][0]
}

function isHorizontal(line) {
    return line[0][1] == line[1][1]
}

function findSlope(line) {
    var xslope = findSlopeHelper(line[1][0] - line[0][0])
    var yslope = findSlopeHelper(line[1][1] - line[0][1])
    return [xslope, yslope]
}

function findSlopeHelper(num) {
    if (num < 0) {
        return -1
    } else if (num > 0) {
        return 1
    } else {
        return 0
    }
}

function plotLineOnGrid(line, type) {
    if (type == 'horizontal' && isHorizontal(line) || 
        type == 'vertical' && isVertical(line) || 
        type == 'diagonal' && ! (isHorizontal(line) || isVertical(line))) {
        // console.log(line)
        // console.log(type)
        // console.log(isHorizontal(line))
        var slope = findSlope(line)
        var i = line[0][0]
        var j = line[0][1]
        while (! (i == line[1][0]+slope[0] && j == line[1][1]+slope[1])) {
            key = [i, j]
            if(key in grid) {
                grid[key] += 1
            } else {
                grid[key] = 1
            }
            i += slope[0]
            j += slope[1]
        }
    }
}

function countIntersections(grid) {
    var overlaps = 0
    for (const [key, value] of Object.entries(grid)) {
        if (value >= 2) {
            overlaps += 1
        }
    } 
    return overlaps
}


var data = readInput('day05.txt').split('\n').map(l => l.split(' -> ').map(e => e.split(',').map(Number)))
var grid = {}

data.forEach(l => plotLineOnGrid(l, 'vertical'))
data.forEach(l => plotLineOnGrid(l, 'horizontal'))
console.log('Part 1:', countIntersections(grid))

data.forEach(l=> plotLineOnGrid(l, 'diagonal'))
console.log('Part 2:', countIntersections(grid))