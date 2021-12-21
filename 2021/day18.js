const assert = require('assert')

const fs = require('fs')
const path = require('path')

function readInput(filename) {
    return fs.readFileSync(path.join('inputs', filename), 'utf8')
}

function part1(input) {
    var final = sum(input)
    return magnitude(eval(final))
}

function part2(input) {
    mags = []
    for (var i=0; i < input.length; i++) {
        for (var j=0; j < input.length; j++) {
            if (i == j) 
                continue
            else {
                mags.push(magnitude(eval(add(input[i], input[j]))))
            }
        }
    }
    return Math.max(...mags)
}

function sum(numbers) {
    var new_number = add(numbers[0], numbers[1])
    for (var i = 2; i < numbers.length; i++) {
        new_number = add(new_number, numbers[i])
    }
    return new_number
}

function add(n1, n2) {
    var n = '[' + String([n1, n2]) + ']'
    return reduce(n)
}

function reduce(number) {
    // Match a a pair 4 times nested down
    var is_nested = nested(number)
    while (is_nested != null) {
        number = explode(number)
        is_nested = nested(number)
    }

    if (number.match(/[0-9]{2,}/g))
        number = split(number)

    if (nested(number) != null || number.match(/[0-9]{2,}/)) 
        return reduce(number)
    else
        return number
}

function nested(number) {
    var level = 0
    for (var i=0; i < number.length; i++) {
        if (number[i] == '[')
            level++
        else if (number[i] == ']')
            level--
        if (level == 5) 
            return i
    }
    return null
}

function explode(number) {
    var m = nested(number)
    var pre_str = number.slice(0, m)
    var str = number.slice(m)

    // Find the first pair within the nested array
    var new_match = str.match(/\[[0-9]+\,[0-9]+\]/)
    var post_str = str.slice(new_match.index + new_match[0].length - 1)
    var pair = eval(new_match[0])

    // Figure out pre string with right-most int added to the left part of the pair
    var left_int_match = pre_str.match(/[0-9]+/g)
    if (left_int_match) {
        var left_int_index = pre_str.lastIndexOf(left_int_match.slice(-1))
        var left_int = Number(pre_str.slice(left_int_index, left_int_index+left_int_match.slice(-1)[0].length)) + pair[0]
        pre_str = pre_str.slice(0, left_int_index) + left_int + pre_str.slice(left_int_index+left_int_match.slice(-1)[0].length)
    }

    // Figure out post string with left-most int added to the right part of the pair
    var right_int_match = post_str.match(/[0-9]+/)
    if (right_int_match) {
        var right_int = parseInt(right_int_match[0]) + pair[1]
        post_str = post_str.slice(1, right_int_match.index) + right_int + post_str.slice(right_int_match.index + right_int_match[0].length)
    } else {
        post_str = post_str.slice(1)
    }

    return pre_str + '0' + post_str
}

function split(number) {
    var m = number.match(/[0-9]{2,}/)
    if (m) {
        var pre_str = number.slice(0, m.index)
        var post_str = number.slice(m.index + m[0].length)
        var n = Number(m[0])
        var pair = '[' + String([Math.floor(n/2), Math.ceil(n/2)]) + ']'
        var new_number = pre_str + pair + post_str
    } else {
        var new_number = number
    }
    return new_number
}

function magnitude(number) {
    if (Array.isArray(number)) {
        return 3 * magnitude(number[0]) + 2 * magnitude(number[1])
    } else {
        return number
    }
}

assert.equal(add('[1,2]', '[[3,4],5]'), '[[1,2],[[3,4],5]]')
assert.equal(explode('[[[[[9,8],1],2],3],4]'), '[[[[0,9],2],3],4]')
assert.equal(explode('[7,[6,[5,[4,[3,2]]]]]'), '[7,[6,[5,[7,0]]]]')
assert.equal(explode('[[6,[5,[4,[3,2]]]],1]'), '[[6,[5,[7,0]]],3]')
assert.equal(explode('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'), '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
assert.equal(explode('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'), '[[3,[2,[8,0]]],[9,[5,[7,0]]]]')

assert.equal(split('[1,[11,10]]'), '[1,[[5,6],10]]')

assert.equal(add('[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]'), '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
assert.equal(add('[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]', '[2,9]'), '[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]')

assert.equal(sum(['[1,1]', '[2,2]', '[3,3]', '[4,4]']), '[[[[1,1],[2,2]],[3,3]],[4,4]]')
assert.equal(sum(['[1,1]', '[2,2]', '[3,3]', '[4,4]', '[5,5]']), '[[[[3,0],[5,3]],[4,4]],[5,5]]')

assert.equal(magnitude([[9,1],[1,9]]), 129)
assert.equal(magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]), 1384)
assert.equal(magnitude([[[[1,1],[2,2]],[3,3]],[4,4]]), 445)
assert.equal(magnitude([[[[3,0],[5,3]],[4,4]],[5,5]]), 791)
assert.equal(magnitude([[[[5,0],[7,4]],[5,5]],[6,6]]), 1137)
assert.equal(magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]), 3488)

// var numbers = readInput('day18_test.txt').split('\n')
var numbers = readInput('day18.txt').split('\n')

console.log('Part 1:', part1(numbers))
console.log('Part 2:', part2(numbers))