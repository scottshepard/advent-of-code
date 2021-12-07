const fs = require('fs')
const path = require('path')

function readInput(filename) {
    return fs.readFileSync(path.join('inputs', filename), 'utf8')
}

// Part 1 - Brute Force
var data = readInput('day06.txt').split(',').map(Number)
for(var j=0; j < 80; j++) {
    var new_fish = 0
    for(var i=0; i < data.length; i++) {
        data[i]--
        if (data[i] == -1) {
            new_fish++
            data[i] = 6
        }
    }
    for(var n=0; n < new_fish; n++) {
        data.push(8)
    }
}
console.log(data.length)

// Part 2
data = readInput('day06.txt').split(',').map(Number)
var fish_buckets = {}
var cycles = 256

for(var j=0; j < 10; j++) {
    var new_fish = 0
    for(var i=0; i < data.length; i++) {
        data[i]--
        if (data[i] == -1) {
            new_fish++
            data[i] = 6
        }
    }
    for(var n=0; n < new_fish; n++) {
        data.push(8)
    }
}
// console.log(data)

for(var i=0; i < data.length; i++) {
    if (data[i] in fish_buckets) {
        fish_buckets[data[i]]++
    } else {
        fish_buckets[data[i]] = 1
    }
}
// console.log(fish_buckets)

for(var j=0; j < 246; j++) {
    var new_fish
    if (0 in fish_buckets) {
        new_fish = fish_buckets[0]
    }
    for(var i=0; i < 8; i++) {
        if (i in fish_buckets) {
            fish_buckets[i] = fish_buckets[i+1]
        }        
    }
    fish_buckets[6] += new_fish
    fish_buckets[8] = new_fish
}

var total = 0
for(f in fish_buckets) {
    total += fish_buckets[f]
}
// console.log(fish_buckets)
console.log(total)
