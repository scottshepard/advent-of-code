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

    def __init__(self, replacements):
        self.replacements = self._parse_replacements(replacements)

    def _parse_replacements(self, replacements_list):
        replacements_dict = {}
        for r in replacements_list:
            r = r.split(' => ')
            if r[0] in replacements_dict.keys():
                replacements_dict[r[0]].append(r[1])
            else:
                replacements_dict[r[0]] = [r[1]]
        return replacements_dict

    def find_all_replacements(self, molecule):
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


    def reverse_search(self, molecule):
        max_len = 0
        max_k = ''
        max_v = ''
        for k, v_l in self.replacements.items():
            for v in v_l:
                if (len(v) > max_len) and (v in molecule):
                    max_len = len(v)
                    max_k = k
                    max_v = v
        molecule = re.sub(max_v, max_k, molecule, 1)
        return molecule

    def count_steps_to_make(self, molecule, count=0):
        molecule = self.reverse_search(molecule)
        count += 1
        if molecule == 'e':
            return count
        else:
            return self.count_steps_to_make(molecule, count)

sample_replacements = [
    'H => HO',
    'H => OH',
    'O => HH',
    'e => H',
    'e => O'
]
sample_molecule = ['HOH', 'HOHOHO']

test_machine = Machine(sample_replacements)
assert len(test_machine.find_all_replacements('HOH')) == 4
assert len(test_machine.find_all_replacements('HOHOHO')) == 7

assert test_machine.count_steps_to_make('HOH') == 3
assert test_machine.count_steps_to_make('HOHOHO') == 6


replacements = read_input('replacements.txt')
molecule = read_input('input.txt')[0]
m = Machine(replacements)
print('Part 1:', len(m.find_all_replacements(molecule)))
print('Part 2:', m.count_steps_to_make(molecule))
