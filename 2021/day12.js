const fs = require('fs')
const path = require('path')

function readInput(filename) {
    return fs.readFileSync(path.join('inputs', filename), 'utf8')
}

var data = readInput('day12.txt').split('\n')

var Cave = function(data) {
    this.map = this.plotMap(data)
    this.paths = []
}

Cave.prototype.plotMap = function (input) {
    var map = {}
    input.forEach(function(e) {
        var arr = e.split('-')
        if (map[arr[0]])
            map[arr[0]].push(arr[1])
        else 
            map[arr[0]] = [arr[1]]    
        if (arr[1] != 'end' && arr[0] != 'start') {
            if (map[arr[1]]) 
                map[arr[1]].push(arr[0])
            else
                map[arr[1]] = [arr[0]]
        }
    })
    return map
}

Cave.prototype.moreThanOneSmallCaveVisitedTwice = function(trail) {
    var smallCavesVisited = {}
    var smallCavesVisitedTwice = 0
    for (var i=0; i < trail.length; i++) {
        var x = trail[i]
        if(x in smallCavesVisited) {
            smallCavesVisited[x] += 1
            if (smallCavesVisited[x] >= 2)
                smallCavesVisitedTwice++
        } else if (isLowerCase(x)) {
            smallCavesVisited[x] = 1
        }
    }
    return smallCavesVisitedTwice > 1
    // return smallCavesVisited
}

Cave.prototype.tracePaths = function(node, part, previous) {
    if (previous == null)
        previous = []
    if (node=='end') {
        var newPrevious = previous.slice()
        newPrevious.push(node)
        this.paths.push(newPrevious)
        return
    } 
    if (part==1 && isLowerCase(node) && previous.includes(node))
        return
    var newPrevious = previous.slice()
    newPrevious.push(node)
    if (part==2 && isLowerCase(node) && (this.moreThanOneSmallCaveVisitedTwice(newPrevious) || countInArray(newPrevious, node)>2))
        return 
    var nextNodes = this.map[node]
    var self = this
    nextNodes.forEach(function(nn) {
        self.tracePaths(nn, part, newPrevious)
    })
}

function isLowerCase(str) {
    return str == str.toLowerCase() && str != str.toUpperCase();
}

function countInArray(array, what) {
    return array.filter(item => item == what).length;
}

var cave = new Cave(data)
console.log(cave.map)
cave.tracePaths('start', 1)
console.log(cave.paths.length)
cave.paths = []
cave.smallCavesVisited = {}
cave.tracePaths('start', 2)
console.log(cave.paths.length)

