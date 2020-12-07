import pandas as pd
import math


class Player:

    def __init__(self, hp, damage, armor):
        self.hp = hp
        self.damage = damage
        self.armor = armor


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play(self):
        self.p1.attack = max([1, self.p1.damage - self.p2.armor])
        self.p2.attack = max([1, self.p2.damage - self.p1.armor])

        p1_turns = math.ceil(self.p1.hp / self.p2.attack)
        p2_turns = math.ceil(self.p2.hp / self.p1.attack)

        return p1_turns >= p2_turns

g1 = Game(Player(8, 5, 5), Player(12, 7, 2))
assert g1.play()

g2 = Game(Player(6, 5, 5), Player(12, 7, 2))
assert not g2.play()


class Shop:

    def __init__(self, items):
        self.items = items
        self.weapons = items[items.type == 'Weapon'].reset_index()
        self.armor = items[items.type=='Armor'].reset_index()
        self.rings = items[items.type=='Ring'].reset_index()

    def generate_all_combos(self):
        columns = ['cost', 'damage', 'armor', 'items']
        combos = pd.DataFrame(columns=columns)
        for i in range(5):
            w = self.weapons.iloc[i]
            #pdb.set_trace()
            row = pd.DataFrame({'cost': w.cost, 'damage': w.damage, 'armor': w.armor, 'items': w['name']}, index=[i])
            combos = pd.concat([combos, row])
            for j in range(5):
                a = self.armor.iloc[j]
                c = pd.concat([a, w])
                row = pd.DataFrame({'cost': c.cost.sum(), 'damage': c.damage.sum(), 'armor': c.armor.sum(), 'items': ','.join(c['name'])}, index=[i+j+1])
                combos = pd.concat([combos, row])
                for k in range(6):
                    r1 = self.rings.iloc[k]
                    c = pd.concat([r1, w])
                    row = pd.DataFrame({'cost': c.cost.sum(), 'damage': c.damage.sum(), 'armor': c.armor.sum(), 'items': ','.join(c['name'])}, index=[i+j+1])
                    combos = pd.concat([combos, row])

                    c = pd.concat([r1, a, w])
                    row = pd.DataFrame({'cost': c.cost.sum(), 'damage': c.damage.sum(), 'armor': c.armor.sum(), 'items': ','.join(c['name'])}, index=[i+j+1])
                    combos = pd.concat([combos, row])
                    for l in range(k+1,6):
                        r2 = self.rings.iloc[l]
                        c = pd.concat([r1, r2, w])
                        row = pd.DataFrame({'cost': c.cost.sum(), 'damage': c.damage.sum(), 'armor': c.armor.sum(), 'items': ','.join(c['name'])}, index=[i+j+1])
                        combos = pd.concat([combos, row])

                        c = pd.concat([r1, r2, a, w])
                        row = pd.DataFrame({'cost': c.cost.sum(), 'damage': c.damage.sum(), 'armor': c.armor.sum(), 'items': ','.join(c['name'])}, index=[i+j+1])
                        combos = pd.concat([combos, row])
        self.combos = combos.reset_index().drop(columns='index')
        return combos

def play(damage, armor):
    boss = Player(109, 8, 2)
    me = Player(100, damage, armor)
    g = Game(me, boss)
    return g.play()

items = pd.read_csv('item_shop.csv')
s = Shop(items)
s.generate_all_combos()

win = []
for i in range(s.combos.shape[0]):
    row = s.combos.iloc[i]
    win.append(play(row['damage'], row['armor']))
s.combos['win'] = win

print('Part 1:', s.combos[s.combos.win].cost.min())
print('Part 2:', s.combos[~s.combos.win].cost.max())
