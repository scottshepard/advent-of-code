const fs = require('fs')
const path = require('path')

function readInput(filename) {
    return fs.readFileSync(path.join('inputs', filename), 'utf8')
}

var data = readInput('day09.txt').split('\n').map(e => e.split('').map(Number))
// console.log(data)

function getSurrondingPoints(x, y) {
    var points = [[x, y-1], [x, y+1], [x+1, y], [x-1, y]]
    var results = []
    for (var i=0; i < points.length; i++) {
        p = points[i]
        if (!(p[0] < 0 || p[0] >= data[0].length || p[1] < 0 || p[1] >= data.length)) {
            results.push(p)
        } 
    }
   return results 
}

var part1_score = 0
var lowPoints = []
for(var j=0; j < data.length; j++) {
    var row = data[j]
    for(var i=0; i < row.length; i++) {
        var compare = getSurrondingPoints(i, j)
        var point = row[i]
        var higher_than = 0
        for(var k=0; k < compare.length; k++) {
            c = compare[k]
            if (point >= data[c[1]][c[0]]) {
                higher_than++
            }
        }
        if (higher_than == 0) {
            part1_score += point + 1
            lowPoints.push([i,j])
        }
    }
}
console.log('Part 1:', part1_score)

function searchBasin(x, y) {
    var point = data[y][x]
    if (data[y][x] == 9)
        return
    var basinPoints = [String([x,y])]
    var compare = getSurrondingPoints(x, y)
    for(var k=0; k < compare.length; k++) {
        c = compare[k]
        if (point < data[c[1]][c[0]]) {
            var newBasinPoints = searchBasin(c[0], c[1])
            if (newBasinPoints) {
                for(var l=0; l < newBasinPoints.length; l++) {
                    if (!(basinPoints.includes(newBasinPoints[l])))
                        basinPoints.push(String(newBasinPoints[l]))
                }
            }
        }
    }
    return basinPoints
}

var basins = []
for(var i=0; i < lowPoints.length; i++) {
    var lp = lowPoints[i]
    basins.push(searchBasin(lp[0], lp[1]).length)
}
topBasins = basins.sort(function(a, b) {return b-a}).slice(0,3)
console.log('Part 2:', topBasins.reduce((a,b) => a*b))