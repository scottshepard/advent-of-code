const fs = require('fs')
var path = require('path')

function readInput(filename) {
    return fs.readFileSync(path.join('inputs', filename), 'utf8')
}

data = readInput('day01.txt')
data = data.split('\n')

data = data.map(element => {
    return parseInt(element)
})

var total = 0
for (var i=0; i < data.length; i++) {
    if (data[i+1] > (data[i])) {
        total += 1
    }
}

console.log('Part 1:', total)

var total = 0
for (var i=0; i < data.length; i++) {
    w1 = data[i] + data[i+1] + data[i+2]
    w2 = data[i+1] + data[i+2] + data[i+3]

    if (w2 > w1) {
        total += 1
    }
}

console.log('Part 2:', total)