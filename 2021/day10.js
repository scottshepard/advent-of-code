const fs = require('fs')
const path = require('path')
const { listenerCount } = require('process')

function readInput(filename) {
    return fs.readFileSync(path.join('inputs', filename), 'utf8')
}

var data = readInput('day10.txt').split('\n')

// console.log(data[0])

function syntaxErrorScore(line) {
    var expected = []
    for(var i = 0; i < line.length; i++) {
        // if the char is an opening bracket, keep track of it's expected closing set
        if('{[<('.includes(line[i])) {
            expected.push(closingChar(line[i]))
        } else {
            // check if the current character matches what is expected
            if (line[i] == expected.slice(-1)[0]) {
                expected.pop()
            } else {
                return {'}':1197, ']':57, '>':25137, ')':3}[line[i]]
            }
        }
    }
    return 0
}

function autoCompleteLine(line) {
    var expected = []
    for(var i = 0; i < line.length; i++) {
        // if the char is an opening bracket, keep track of it's expected closing set
        if('{[<('.includes(line[i])) {
            expected.push(closingChar(line[i])) 
        } else {
            // check if the current character matches what is expected
            if (line[i] == expected.slice(-1)[0])
                expected.pop()           
        }
    }
    return expected.reverse().join('')
}

function autoCompleteScore(completion_string) {
    var total = 0 
    for(var i=0; i < completion_string.length; i++) {
        var char = completion_string[i]
        total *= 5
        total += {')':1, ']':2, '}':3, '>':4}[char]
    }
    return total
}

function closingChar(char) {
    return {'{':'}', '[': ']', '<':'>', '(':')'}[char]
}

function part1(data) {
    var score = 0
    for(var i=0; i < data.length; i++) 
        score += syntaxErrorScore(data[i])
    return score
}

function part2(data) {
    var scores = []
    for(var i=0; i < data.length; i++) {
        if (syntaxErrorScore(data[i]) == 0) {
            scores.push(autoCompleteScore(autoCompleteLine(data[i])))
        }
    }
    return scores.sort(function(a, b) {return a-b})[parseInt(scores.length / 2)]
    // return scores
}

console.log('Part 1:', part1(data))
console.log('Part 2:', part2(data))
