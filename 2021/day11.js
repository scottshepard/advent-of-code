const fs = require('fs')
const path = require('path')
const { listenerCount } = require('process')

function readInput(filename) {
    return fs.readFileSync(path.join('inputs', filename), 'utf8')
}

var data = readInput('day11.txt').split('\n').map(e => e.split('').map(Number))

class GameOfLife {
    constructor(data) {
        this.grid = data.map(x => x)
        this.height = data.length
        this.width = data[0].length
        this.size = this.height * this.width
        this.flashes = 0
        this.steps = 0
    }

    next() {
        var flashPoints = []
        var flashes = 0
        for (var j=0; j < this.height; j++) {
            for (var i=0; i < this.width; i++) {
                this.grid[j][i]++
                if (this.grid[j][i] == 10)
                    flashPoints.push([i,j])
            }
        }
        while (flashPoints.length > 0) {
            var fp = flashPoints.pop()
            var newFlashPoints = this.flash(fp[0], fp[1])
            while (newFlashPoints.length > 0)
                flashPoints.push(newFlashPoints.pop())
        }
        for (var j=0; j < this.height; j++) {
            for (var i=0; i < this.width; i++) {
                if (this.grid[j][i] > 9) {
                    this.grid[j][i] = 0
                    flashes += 1
                }
            }
        }
        this.flashes += flashes
        this.steps++
        return flashes
    }

    flash(x, y) {
        var newFlashPoints = []
        for (var i=-1; i < 2; i++) {
            for (var j=-1; j < 2; j++) {
                if (this.grid[y+j] && this.grid[y+j][x+i]) {
                    this.grid[y+j][x+i]++
                    if (this.grid[y+j][x+i] == 10) {
                        newFlashPoints.push([x+i, y+j])
                    }
                }
            }
        }
        return newFlashPoints
    }

    synchronize() {
        var steps = 0
        var flashes = 0
        while (flashes < this.size) {
            flashes = this.next()
            steps++
        }
        return steps
    }
}
 
function solve(data) {
    let g = new GameOfLife(data)
    for (var i=0; i < 100; i++) {
        g.next()
    }
    console.log('Part 1:', g.flashes)

    g.synchronize()
    console.log('Part 2:', g.steps)
}

solve(data)