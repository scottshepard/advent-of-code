import os


def read_input(file, split_char='\n\n'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs/{0}".format(file))
    f = open(file_path)
    data = f.read().split(split_char)
    if data[-1] == '':
        data.pop(-1)
    return [d.split('\n') for d in data]

sample_rules, sample_input = read_input('day19_test.txt')

class MessageValidator:

    def __init__(self, rules):
        self.rules = self._create_rules(rules)

    def _create_rules(self, rules_list):
        rules_dict = {}
        for line in rules_list:
            root, rule_sets = line.split(':')
            root = int(root)
            rule_sets = rule_sets.split('|')
            for rs in rule_sets:
                rs = rs.strip()
                rs = rs.split(' ')
                if rs[0] in ['"a"', '"b"']:
                    rule = eval(rs[0])
                else:
                    rule = [int(r) for r in rs]
                if root in rules_dict:
                    rules_dict[root].append(rule)
                else:
                    rules_dict[root] = [rule]
        return rules_dict

mv = MessageValidator(sample_rules)




