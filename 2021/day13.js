const fs = require('fs')
const path = require('path')

function readInput(filename) {
    return fs.readFileSync(path.join('inputs', filename), 'utf8')
}

var data = readInput('day13.txt').split('\n\n')
var points = data[0].split('\n')
var folds = data[1].split('\n') 

function fold_hamburger(y) {
    var remove_list = []
    for (var i=0; i < points.length; i++) {
        p = points[i].split(',').map(Number)
        if (p[1] == y) {
            remove_list.push(i)
        } else if (p[1] > y) {
            remove_list.push(i) 
            var newPoint = String([p[0], 2*y-p[1]])
            if (!points.includes(newPoint))
                points.push(newPoint)
        }
    }
    var newPoints = []
    for (var i=0; i < points.length; i++) {
        if (!(remove_list.includes(i)))
            newPoints.push(points[i])
    }
    return newPoints
}

function fold_hotdog(x) {
    var remove_list = []
    for (var i=0; i < points.length; i++) {
        p = points[i].split(',').map(Number)
        if (p[0] == x) {
            remove_list.push(i)
        } else if (p[0] > x) {
            remove_list.push(i) 
            var newPoint = String([2*x-p[0], p[1]])
            if (!points.includes(newPoint))
                points.push(newPoint)
        }
    }
    var newPoints = []
    for (var i=0; i < points.length; i++) {
        if (!(remove_list.includes(i)))
            newPoints.push(points[i])
    }
    return newPoints
}

// DO all the folds
for (var f=0; f < folds.length; f++) {
    fold = folds[f].split(' ')[2].split('=')
    if (fold[0] == 'x') {
        points = fold_hotdog(parseInt(fold[1]))
    } else if (fold[0] == 'y') {
        points = fold_hamburger(parseInt(fold[1]))
    }
    if (f == 0) 
        console.log('Part 1:', points.length) 
}

// Find size of page
var max_x = 0
var max_y = 0
for(var p=0; p < points.length; p++) {
    point = points[p]
    point = point.split(',').map(Number)
    if (point[0] > max_x)
        max_x = point[0]
    if (point[1] > max_y)
        max_y = point[1]
}

// Create an empty 2D array to display message
// Array.fill doesn't work because of copy by reference
var row = []
for (var x=0; x <= max_x; x++) {
    row.push(' ')
}
var manual = []
for (var y=0; y <= max_y; y++) {
    manual.push(row.slice())
}

// Fill the 2D array
for(var p=0; p < points.length; p++) {
    point = points[p]
    point = point.split(',').map(Number)
    manual[point[1]][point[0]] = 'X'
}

for(var r = 0; r < manual.length; r++) {
    manual[r] = manual[r].join('')
}
manual = manual.join('\n')
console.log('Part 2:')
console.log(manual)