import os
import re
import pdb


def read_input(file, split_char='\n'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    f = open(file_path)
    data = f.read().split(split_char)
    if data[-1] == '':
        data.pop(-1)
    return data


class Machine:

    def __init__(self, replacements, starters):
        self.replacements = self._parse_replacements(replacements)
        self.starters = starters

    def _parse_replacements(self, replacements_list):
        replacements_dict = {}
        for r in replacements_list:
            r = r.split(' => ')
            if r[0] in replacements_dict.keys():
                replacements_dict[r[0]].append(r[1])
            else:
                replacements_dict[r[0]] = [r[1]]
        return replacements_dict

    def replace(self, molecule):
        results = []
        for k, v_l in self.replacements.items():
            for v in v_l:
                where = [match.start() for match in re.finditer(k, molecule)]
                for w in where:
                    before = molecule[:w]
                    after = molecule[w:]
                    after = after.replace(k, v, 1)
                    results.append(before + after)
        return set(results)

    def replace_reverse(self, molecule):
        results = []
        for k, v_l in self.replacements.items():
            for v in v_l:
                where = [match.start() for match in re.finditer(v, molecule)]
                for w in where:
                    before = molecule[:w]
                    after = molecule[w:]
                    after = after.replace(v, k, 1)
                    results.append(before + after)
        return set(results)

    def make(self, mol_lst, count=0):
        mols = []
        for mol in mol_lst:
            mols.extend(list(self.replace_reverse(mol)))
        mols = list(set(mols))
        count += 1
        pdb.set_trace()
        for st in self.starters:
            if st in mols:
                return count+1
        else:
            return self.make(mols, count)

sample_replacements = [
    'H => HO',
    'H => OH',
    'O => HH'
]
sample_molecule = ['HOH', 'HOHOHO']

test_machine = Machine(sample_replacements, ['O', 'H'])
assert len(test_machine.replace('HOH')) == 4
assert len(test_machine.replace('HOHOHO')) == 7

#assert test_machine.make(['HOH']) == 3
#assert test_machine.make(['HOHOHO']) == 6


replacements = read_input('replacements.txt')
molecule = read_input('input.txt')[0]
m = Machine(replacements, ['HF', 'NAl', 'OMg'])
print('Part 1:', len(m.replace(molecule)))
print('Part 2:', m.make([molecule]))

