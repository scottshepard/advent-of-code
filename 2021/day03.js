const fs = require('fs')
const path = require('path')

function readInput(filename) {
    return fs.readFileSync(path.join('inputs', filename), 'utf8')
}

data = readInput('day03.txt').split('\n').map(e => e.split(''))

gamma_rate = []
epsilon_rate = []
for (i=0; i < data[0].length; i++) {
    let count0 = 0
    let count1 = 0
    for (j=0; j < data.length; j++) {
        if (data[j][i] == '0') {
            count0 += 1
        } else if (data[j][i] == '1') {
            count1 += 1
        }
    }
    if (count0 > count1) {
        gamma_rate.push(0)
        epsilon_rate.push(1)
    } else {
        gamma_rate.push(1)
        epsilon_rate.push(0)
    }
}
gamma_rate = parseInt(gamma_rate.join(''), 2)
epsilon_rate= parseInt(epsilon_rate.join(''), 2)

console.log('Part 1:', gamma_rate * epsilon_rate)

// Part 2
function mostLeastBit(data, pos, type) {
    let count0 = 0
    let count1 = 0
    for (j=0; j < data.length; j++) {
        if (data[j][pos] == '0') {
            count0 += 1
        } else if (data[j][pos] == '1') {
            count1 += 1
        }
    }
    if (count0 > count1) {
        if (type == 'most') {
            return '0'
        } else {
            return '1'
        }
    } else {
        if (type == 'most') {
            return '1'
        } else {
            return '0'
        }
    }
}

function removeElements(dat, bit, pos) {
    let j = 0
    while (j < dat.length) {
        if (dat.length == 1) {
            return data
        }
        else if (dat[j][pos] != bit) {
            dat.splice(j, 1)
            j -= 1
        }
        j += 1
    }
    return dat
}


let data_most  = readInput('day03.txt').split('\n').map(e => e.split('')) 
let data_least = readInput('day03.txt').split('\n').map(e => e.split('')) 
for (i=0; i < data_most[0].length; i++) {
    bit_most  = mostLeastBit(data_most, i, 'most')
    bit_least = mostLeastBit(data_least, i, 'least')
    removeElements(data_most, bit_most, i)
    removeElements(data_least, bit_least, i)
}
const O2_RATING  = parseInt(data_most[0].join(''), 2)
const CO2_RATING = parseInt(data_least[0].join(''), 2)
console.log('Part 2:', O2_RATING * CO2_RATING)