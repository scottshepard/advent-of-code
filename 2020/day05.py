from utils import read_input

input = read_input('day05.txt')


def search_once(char, front, back):
    half = int((back - front + 1) / 2)
    if (char == 'F') | (char == 'L'):
        return front, back-half
    elif (char == 'B') | (char == 'R'):
        return front + half, back

assert search_once('F', 0, 127) == (0, 63)

def search(str):
    start_row, end_row = 0, 127
    for r in str[:7]:
        start_row, end_row = search_once(r, start_row, end_row)
    start_col, end_col = 0, 7
    for c in str[-3:]:
        start_col, end_col = search_once(c, start_col, end_col)
    return end_row, end_col

assert search('FBFBBFFRLR') == (44, 5)

def seat_id(str):
    row, col = search(str)
    return row * 8 + col

assert seat_id('FBFBBFFRLR') == 357


print('Part 1:', max([seat_id(bp) for bp in input]))

manifest = {search(bp): seat_id(bp) for bp in input}

occupied_seats = list(manifest.keys())

unoccupied_seats = []
for r in range(127):
    for c in range(7):
        if (r,c) not in occupied_seats:
            unoccupied_seats.append((r,c))



for seat in unoccupied_seats:
    r, c = seat
    id = r * 8 + c
    if ((id + 1) in manifest.values()) & ((id-1) in manifest.values()):
        ans = id
print('Part 2:', ans)

