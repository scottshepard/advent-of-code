const assert = require('assert')
const fs = require('fs')
const path = require('path')


class Game {
    constructor(p1, p2) {
        this.p1_pos = p1
        this.p1_score = 0
        this.p2_pos = p2
        this.p2_score = 0
        this.die = 1
        this.nDieRolls = 0
        this.winner = ''
    }

    play() {
        while (this.winner == '') {
            this.takeTurn()
        }
        if (this.winner == 'Player 1') {
            var score = this.p2_score * this.nDieRolls
        }
        else
            var score = this.p1_score * this.nDieRolls
        return score
    }
    
    move(pos, die) {
        pos = pos + die
        if (pos > 10)
            pos = pos % 10
        if (pos == 0) 
            pos = 10
        return pos
    }

    takeTurn() {
        var dieSum = 0
        for (var i=0; i < 3; i++) {
            dieSum += this.die
            this.incrementDie()
        }
        this.p1_pos = this.move(this.p1_pos, dieSum)
        this.p1_score += this.p1_pos
        if (this.p1_score >= 1000) {
            this.winner = 'Player 1'
            return 
        }
        dieSum = 0
        for (var i=0; i < 3; i++) {
            dieSum += this.die
            this.incrementDie()
        }
        this.p2_pos = this.move(this.p2_pos, dieSum)
        this.p2_score += this.p2_pos
        if (this.p2_score >= 1000) {
            this.winner = 'Player 2'
            return 
        }
    }

    incrementDie() {
        this.die++
        this.nDieRolls++
        if (this.die > 100)
            this.die = 1
    }
}

// players = [4, 8]
players = [1, 6]
g = new Game(players[0], players[1])
// g.takeTurn()
// console.log(g)
console.log(g.play())