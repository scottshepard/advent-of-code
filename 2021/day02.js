const { log } = require('console')
const fs = require('fs')
var path = require('path')

function readInput(filename) {
    return fs.readFileSync(path.join('inputs', filename), 'utf8')
}

function parseElement(element) {
    let l = element.split(' ')
    l[1] = parseInt(l[1])
    return l
}

data = readInput('day02.txt').split('\n')
data = data.map(parseElement)

// Part 1
let horiz = 0
let depth = 0
data.forEach(d => {
    switch (d[0]) {
        case 'forward':
            horiz += d[1]
            break
        case 'up':
            depth -= d[1]
            break
        case 'down':
            depth += d[1]
            break
    }
})

console.log('Part 1:', horiz*depth)

// Part 2
horiz = 0
depth = 0
let aim = 0
data.forEach(d => {
    switch (d[0]) {
        case 'forward':
            horiz += d[1]
            depth += d[1] * aim
            break
        case 'up':
            aim -= d[1]
            break
        case 'down':
            aim += d[1]
            break
    }
})

console.log('Part 2:', horiz*depth)
