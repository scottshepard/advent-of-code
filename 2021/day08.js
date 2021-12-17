const fs = require('fs')
const path = require('path')

function readInput(filename) {
    return fs.readFileSync(path.join('inputs', filename), 'utf8')
}

var data = readInput('day08.txt').split('\n').map(l => l.split(' | ').map(e => e.split(' ')))

var DIGITMAP = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

count_1478 = 0
for (var i=0; i < data.length; i++) {
    var line = data[i]
    for (var j=0; j < line[1].length; j++) {
        if ([2,3,4,7].includes(line[1][j].length)) 
            count_1478++
    }
}
console.log('Part 1:', count_1478)

function findMissing(a, b) {
    // Returns values in b that are not present in a
    out = ['']
    for (var i=0; i < b.length; i++) {
        if (! a.includes(b[i]))
            out.push(b[i])
    }
    return out.join('')
}

console.log('Should return "e": ', findMissing('abg', 'abeg'))
console.log('Should return "f": ', findMissing('abcde', 'ef'))

// Part 2
function solve(line) {
    var inputs = line[0]
    var sigs = {}
    var sig_map = {}
    var digits = {}
    for (var i=0; i < inputs.length; i++) {
        inputs[i] = inputs[i].split('').sort().join('')
        len = inputs[i].length
        if (len == 2)
            digits[inputs[i]] = 1
        else if (len == 4)
            digits[inputs[i]] = 4
        else if (len == 3)
            digits[inputs[i]] = 7
        else if (len == 7) 
            digits[inputs[i]] = 8

        if (len in sigs) 
            sigs[len].push(inputs[i])
        else
            sigs[len] = [inputs[i]]
    }

    // Rule 1: One six-length does not fully overlap with the 2-length. The missing char is 'c'. The six-length is 6.
    for (var i=0; i < sigs[6].length; i++) {
        x = findMissing(sigs[6][i], sigs[2][0])
        if (x != '') {
            sig_map['c'] = x    
            digits[sigs[6][i]] = 6
        }
    }

    // Rule 2: Remaining unknown char in 2 (2-length str) must be 'f'
    sig_map['f'] = findMissing(sig_map['c'], sigs[2][0])

    // Rule 3: One six-length minus CF and the chars in 4 is also missing D. The six-lenght is 0.
    for (var i=0; i < sigs[6].length; i++) {
        x = findMissing(sigs[6][i], sigs[4][0])
        if (x != '' && x != sig_map['c']) {
            sig_map['d'] = x
            digits[sigs[6][i]] = 0
        }
    }

    // Rule 4: Remaining unknow char in 4 is 'b'
    sig_map['b'] = findMissing([sig_map['c'], sig_map['d'], sig_map['f']].join(''), sigs[4][0])

    // Rule 5: The last unknown six-lenght is 9. It's missing char is 'e'
    nine_sig = findMissing(Object.keys(digits), sigs[6])
    sig_map['e'] = findMissing(nine_sig, 'abcdefg')
    digits[nine_sig] = 9

    // Rule 6: Last uknown char in three-length is 'a'
    sig_map['a'] = findMissing(sigs[2][0], sigs[3][0])

    // Rule 7: Last unknow character is 'g'
    sig_map['g'] = findMissing(Object.values(sig_map).join(''), 'abcdefg')

    // Fill in remaining digits values, the 5s
    for (var i=0; i < sigs[5].length; i++) {
        digits[sigs[5][i]] = digit(sigs[5][i], sig_map)
    }

    var output = []
    for (var i=0; i < line[1].length; i++) {
        output.push(digits[line[1][i].split('').sort().join('')])
    }
    return parseInt(output.join(''))
}

function digit(signal, sig_map) {
    sig_map = invertDict(sig_map)
    var translated = []
    for (var i=0; i < signal.length; i++) 
        translated.push(sig_map[signal[i]])
    return DIGITMAP[translated.sort().join('')]
}

function invertDict(dict) {
    var newDict = {}
    for (key in dict) 
        newDict[dict[key]] = key
    return newDict 
}

var sum = 0
for (var i=0; i < data.length; i++) {
    sum += solve(data[i])
}

console.log('Part 2: ', sum)