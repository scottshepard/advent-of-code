from utils import read_input
import pdb

input = read_input('day04.txt')

part1 = 0
cards = {}
for line in input:
    card, winners = line.split('|')
    num, card = card.split(':')
    num = int(num.replace('Card ', ''))
    card = [int(c) for c in card.split(' ') if c != '']
    winners = [int(w) for w in winners.split(' ') if w != '']
    cards[num] = [card, winners, 1]
    matches = [c for c in card if c in winners]
    if len(matches) > 0:
        # pdb.set_trace()
        part1 += 2**(len(matches)-1)

part2 = 0
for num in cards:
    card, winners, _ = cards[num]
    matches = [c for c in card if c in winners]
    for i in range(1, len(matches)+1):
        # print(i)
        if num+i >= len(cards):
            break
        cards[num+i][2] += cards[num][2]
    part2 += cards[num][2]


print(part1)
print(part2)


