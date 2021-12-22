const assert = require('assert')
const { getCipherInfo } = require('crypto')

const fs = require('fs')
const path = require('path')
const { runInThisContext } = require('vm')

function readInput(filename) {
    return fs.readFileSync(path.join('inputs', filename), 'utf8')
}



class Trench {
    constructor(image_text, mask) {
        this.image = this.parseImage(image_text)
        this.mask = mask
        this.determineImageBounds()
    }

    parseImage(image_text) {
        var image = {}
        image_text = image_text.split('\n')
        for (var j=0; j < image_text.length; j++) {
            for (var i=0; i < image_text[0].length; i++) {
                image[String([i, j])] = image_text[j][i]
            }
        }
        this.minx = 0
        this.maxx = image_text.length-1
        this.miny = 0
        this.maxy = image_text[0].length-1
        return image
    }

    determineImageBounds() {
        var xlist = []
        var ylist = []
        for (var xy in this.image) {
            if (this.image[xy] == '#') {
                xy = xy.split(',').map(Number)
                xlist.push(xy[0])
                ylist.push(xy[1])
            }
        } 
        this.minx = Math.min(...xlist)
        this.miny = Math.min(...ylist)
        this.maxx = Math.max(...xlist)
        this.maxy = Math.max(...ylist)
    }

    enchance(step) {
        var new_image = {}
        for (var j=this.miny-2; j < this.maxy+3; j++) {
            for (var i=this.minx-2; i < this.maxx+3; i++) {
                var xy = String([i,j])
                new_image[xy] = this.mask[this.getBinaryNumber(xy, step)]
            }
        }
        this.image = new_image
        this.miny -= 3
        this.minx -= 3
        this.maxy += 3
        this.maxx += 3
    }

    getBinaryNumber(xy, step) {
        var pixelMap = {'.': '0', '#': '1'}
        var pixels = []
        xy = xy.split(',').map(Number)
        for (var j = -1; j < 2; j++) {
            for (var i = -1; i < 2; i++) {
                var c = String([xy[0]+i, xy[1]+j])
                if (c in this.image)
                    pixels.push(pixelMap[this.image[c]])
                else {
                    if (step % 2 == 0)
                        pixels.push('0')
                    else
                        pixels.push('1')
                }
            }
        }
        return parseInt(pixels.join(''), 2)
    }

    countPixels() {
        var count = 0
        for (var xy in this.image) {
            if (this.image[xy] == '#')
                count++
        }
        return count
    }
}

var data = readInput('day20.txt').split('\n\n')
t = new Trench(data[1], data[0])

for (var i=0; i < 50; i++) {
    t.enchance(i)
    if (i == 1) 
        console.log('Part 1:', t.countPixels())
}
console.log('Part 2:', t.countPixels())
