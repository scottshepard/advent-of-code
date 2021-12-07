const fs = require('fs')
const path = require('path')

function readInput(filename) {
    return fs.readFileSync(path.join('inputs', filename), 'utf8')
}

var data = readInput('day07.txt').split(',').map(Number)


// var data = '16,1,2,0,4,2,7,1,2,14'.split(',').map(Number)
data.sort(function(a, b) {return a-b}) // JS native sort doesn't sort integers well
var pos = data[data.length/2]

function fuelCost(x) {
    var sum = 0
    for (i in data) {
        sum += Math.abs(data[i] - x)
    }
    return sum
}

console.log('Part 1:', fuelCost(pos))

function fuelCostForCrab(dist) {
    return (dist + 1) * (dist / 2)
}

function fuelCost2(x) {
    var sum = 0
    for (i in data) {
        sum += fuelCostForCrab(Math.abs(data[i]-x))
    }
    return sum
}

cost_here = fuelCost2(pos)
cost_next = fuelCost2(pos+1)
while (cost_here > cost_next) {
    pos++
    cost_here = fuelCost2(pos)
    cost_next = fuelCost2(pos+1)
}
console.log('Part 2:', cost_here)