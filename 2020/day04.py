from utils import read_input
import re
import numpy as np
import pdb


input = read_input('day04.txt', '\n\n')


required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

n_valid_passports = 0
for passport in input:
    if all([k in passport for k in required_keys]):
        n_valid_passports += 1
print('Part 1: ', n_valid_passports)

def extract(pattern, string):
    try:
        found = re.search(pattern, string).group(1)
    except:
        found = ''
    return found

def is_valid_passport(raw_passport):
    return passport_checker(passport_parser(raw_passport))


def passport_parser(raw_passport):
    byr = extract('byr:([0-9]{4})', raw_passport)
    iyr = extract('iyr:([0-9]{4})', raw_passport)
    eyr = extract('eyr:([0-9]{4})', raw_passport)
    hgt = extract('hgt:([0-9]+(in|cm))', raw_passport)
    hcl = extract('hcl:(#[0-9a-f]{6})', raw_passport)
    ecl = extract('ecl:([a-z]{3})', raw_passport)
    pid = extract('pid:([0-9]{9})', raw_passport)
    return {'byr':byr, 'iyr':iyr, 'eyr':eyr, 'hgt':hgt, 'hcl':hcl, 'ecl':ecl, 'pid':pid}

def passport_checker(parsed_passport):
    pp = parsed_passport
    if '' in pp.values():
        return False
    else:
        valid_byr = 1920 <= int(pp['byr']) <= 2002
        valid_iyr = 2010 <= int(pp['iyr']) <= 2020
        valid_eyr = 2020 <= int(pp['eyr']) <= 2030
        valid_hgt = _valid_height(pp['hgt'])
        valid_ecl = pp['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        #pdb.set_trace()
        return (valid_byr and valid_iyr and valid_eyr and valid_hgt and valid_ecl)

def _valid_height(hgt_str):
    hgt = int(extract('([0-9]+)', hgt_str))
    if 'in' in hgt_str:
        return 59 <= hgt <= 76
    elif 'cm' in hgt_str:
        return 150 <= hgt <= 193
    else:
        return False


invalid_tests = [
    'eyr:1972 cid:100\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',
    'iyr:2019\nhcl:#602927 eyr:1967 hgt:170cm\necl:grn pid:012533040 byr:1946',
    'hcl:dab227 iyr:2012\necl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',
    'hgt:59cm ecl:zzz\neyr:2038 hcl:74454a iyr:2023\npid:3556412378 byr:2007'
]

valid_tests = [
    'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\nhcl:#623a2f',
    'eyr:2029 ecl:blu cid:129 byr:1989\niyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
    'hcl:#888785\nhgt:164cm byr:2001 iyr:2015 cid:88\npid:545766238 ecl:hzl\neyr:2022',
    'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'
]

for test in invalid_tests:
    assert not passport_checker(passport_parser(test))

for test in valid_tests:
    assert passport_checker(passport_parser(test))

print('Part 2:', sum([is_valid_passport(passport) for passport in input]))
print('Part 2 answer was actually 153. Still not sure which one is off.')
