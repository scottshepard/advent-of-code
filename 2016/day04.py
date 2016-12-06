# --- Day 4: Security Through Obscurity ---
#
# Finally, you come across an information kiosk with a list of rooms. 
# Of course, the list is encrypted and full of decoy data, but the instructions
# to decode the list are barely hidden nearby. Better remove the decoy data 
# first.
#
# Each room consists of an encrypted name (lowercase letters separated by 
# dashes) followed by a dash, a sector ID, and a checksum in square brackets.
#
# A room is real (not a decoy) if the checksum is the five most common letters 
# in the encrypted name, in order, with ties broken by alphabetization. 
# For example:
#
# aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are
# a (5), b (3), and then a tie between x, y, and z, which are listed 
# alphabetically.
# a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are 
# all tied (1 of each), the first five are listed alphabetically.
# not-a-real-room-404[oarel] is a real room.
# totally-real-room-200[decoy] is not.
# Of the real rooms from the list above, the sum of their sector IDs is 1514.
#
# What is the sum of the sector IDs of the real rooms?
#
# --- Part Two ---
#
# With all the decoy data out of the way, it's time to decrypt this list and 
# get moving.
#
# The room names are encrypted by a state-of-the-art shift cipher, which is 
# nearly unbreakable without the right software. However, the information kiosk
# designers at Easter Bunny HQ were not expecting to deal with a master 
# cryptographer like yourself.
#
# To decrypt a room name, rotate each letter forward through the alphabet a 
# number of times equal to the room's sector ID. A becomes B, B becomes C, Z 
# becomes A, and so on. Dashes become spaces.
#
# For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name
#
# What is the sector ID of the room where North Pole objects are stored?
# ----------------------------------------------------------------------------

from collections import defaultdict
import re
from string import ascii_lowercase

letters = list(ascii_lowercase)

def real_room(encrypted_name, checksum):
    return common_five(encrypted_name) == checksum

def common_five(string):
    charlist = re.findall('[a-z]', string)
    ft = freq_table(charlist)
    top5 = sorted(ft.items(), key=lambda x: (-x[1], x[0]))[:5]
    return ''.join([key for key, value in top5])

def freq_table(list):
    d = defaultdict(int)
    for l in list:
        d[l] += 1
    return d

def parse_line(line):
    room_name = re.match('.+(?=\-[0-9])', line).group(0)
    checksum = re.search(r'\[([A-Za-z0-9_]+)\]', line).group(1)
    sector_id = re.search('[0-9]+', line).group(0)
    return room_name, checksum, sector_id

def rotate_letter(letter, n_rotations):
    if(letter == '-'):
        return ' '
    else:
        i = (letters.index(letter) + n_rotations) % len(letters)
        return letters[i]

def rotate_room_name(room_name, n_rotations):
    room_name = list(room_name)
    if(room_name[len(room_name)-1] == '-'):
        room_name.pop()
    return ''.join([rotate_letter(l, n_rotations) for l in room_name])

if __name__ == '__main__':
    fileobject = open('inputs/day04.txt')
    data = fileobject.read()
    data = re.split('\n', data)
    sectorsum = 0
    roomcheck = []
    rooms = []
    for line in data:
        name, cs, sector_id = parse_line(line)
        if(real_room(name, cs)):
            sector_id= int(sector_id)
            sectorsum += sector_id
            rooms.append((rotate_room_name(name, sector_id), sector_id))
        roomcheck.append(real_room(name, cs))
    sector_id = [s for n, s in rooms if n == 'northpole object storage']
    print("Part 1 - Sum of sector_ids of valid rooms:", sectorsum)
    # Correct answer is 278221
    print("Part 2 - sector_id of northpole object storage room", sector_id)
    # Correct answer is 267

