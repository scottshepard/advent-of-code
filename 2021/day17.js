// var TARGET = {'x': [20, 30], 'y': [-10, -5]}
var TARGET = {'x': [70, 125], 'y': [-159, -121]}

class Probe {
    constructor(vx, vy) {
        this.x = 0
        this.y = 0
        this.maxy = 0
        this.vx = vx
        this.vy = vy
    }

    willHitTarget() {
        var moving = true
        while (true) {
            this.step()
            if (this.hitTarget()) {
                return true
            } else if (this.pastTarget()) {
                return false
            }
        }
    }

    step() {
        this.x += this.vx
        this.y += this.vy
        if (this.y > this.maxy)
            this.maxy = this.y
        this.vx -= Math.sign(this.vx)*1
        this.vy -= 1
        return this.hitTarget()
    }

    hitTarget() {
        return (
            this.x >= TARGET['x'][0] && this.x <= TARGET['x'][1] &&
            this.y >= TARGET['y'][0] && this.y <= TARGET['y'][1]
        )
    }

    pastTarget() {
        return (
            (this.x > TARGET['x'][1] && this.vx >= 0) || 
            (this.y < TARGET['y'][0] && this.vy < 0)
        )
    }
}

console.log('Test cases')
p = new Probe(7, 2)
console.log('(7, 2) should return true: ', p.willHitTarget())
p = new Probe(6, 3)
console.log('(6, 3) should return true: ', p.willHitTarget())
p = new Probe(9, 0)
console.log('(9, 0) return true: ', p.willHitTarget())
p = new Probe(17, -4)
console.log('(17, -4) return false: ', p.willHitTarget())


function willVXWork(vx) {
    TARGET['x'][0]
    var x = 0

    function stepX() {
        x += vx
        vx -= Math.sign(vx)*1
    }

    var hit = false
    var tooShort = false
    var tooFar = false
    while (true) {
        hit = (x >= TARGET['x'][0] && x <= TARGET['x'][1])
        tooShort = (x < TARGET['x'][0] && vx == 0)
        tooFar = (x > TARGET['x'][1])
        stepX()
        if (hit || tooShort)
            break
    }

    return hit
}

function solve() {

    // find the minimum VX that will work
    var min_vx = 0
    var solved = false
    while (!(solved)) {
        min_vx++ 
        solved = willVXWork(min_vx)
    }
    // console.log(minimum_vx)
    var max_vx = TARGET['x'][1]
    var min_vy = TARGET['y'][0]
    // had to look this one up
    var max_vy = Math.max(Math.abs(TARGET['y'][0], Math.abs(TARGET['y'][1])))

    var max_y = 0
    var count = 0
    // Search all possibilites within the bounds
    for (var vx=min_vx; vx < max_vx+1; vx++) {
        for (var vy=min_vy; vy < max_vy+1; vy++) {
            var p = new Probe(vx, vy)
            var isSolution = p.willHitTarget()
            if (isSolution) {
                count++ 
                if (max_y < p.maxy)
                    max_y = p.maxy
            }
        }
    }
    console.log('Part 1:', max_y)
    console.log('Part 2:', count)

    return [max_y, count]
}

solve()


