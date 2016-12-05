# --- Day 5: How About a Nice Game of Chess? ---
#
# You are faced with a security door designed by Easter Bunny engineers that 
# seem to have acquired most of their security knowledge by watching hacking 
# movies.
#
# The eight-character password for the door is generated one character at a 
# time by finding the MD5 hash of some Door ID (your puzzle input) and an 
# increasing integer index (starting with 0).
#
# A hash indicates the next character in the password if its hexadecimal 
# representation starts with five zeroes. If it does, the sixth character in 
# the hash is the next character of the password.
#
# For example, if the Door ID is abc:
#
# The first index which produces a hash that starts with five zeroes is 
# 3231929, wwhich we find by hashing abc3231929; the sixth character of the 
# hash, and thus the first character of the password, is 1.
# 5017308 produces the next interesting hash, which starts with 000008f82..., 
# so the second character of the password is 8.
# The third time a hash starts with five zeroes is for abc5278568, discovering 
# the character f.
# In this example, after continuing this search a total of eight times, the 
# password is 18f47a30.
#
# Given the actual Door ID, what is the password?
#
# --- Part Two ---
# 
# As the door slides open, you are presented with a second door that uses a 
# slightly more inspired security mechanism. Clearly unimpressed by the last 
# version (in what movie is the password decrypted in order?!), 
# the Easter Bunny engineers have worked out a better solution.
# 
# Instead of simply filling in the password from left to right, the hash now 
# also indicates the position within the password to fill. You still look for 
# hashes that begin with five zeroes; however, now, the sixth character 
# represents the position (0-7), and the seventh character is the character 
# to put in that position.
#
# A hash result of 000001f means that f is the second character in the password
# Use only the first result for each position, and ignore invalid positions.
#
#
# For example, if the Door ID is abc:
#
# The first interesting hash is from abc3231929, which produces 0000015...; 
# so, 5 goes in position 1: _5______.
# In the previous method, 5017308 produced an interesting hash; however, 
# it is ignored, because it specifies an invalid position (8).
# The second interesting hash is at index 5357525, which produces 000004e...; 
# so, e goes in position 4: _5__e___.
# You almost choke on your popcorn as the final character falls into place, 
# producing the password 05ace8e3.
#
# Given the actual Door ID and this new method, what is the password? 
# Be extra proud of your solution if it uses a cinematic "decrypting" animation
#
# ----------------------------------------------------------------------------
#
# To run this script, you need to input the text string on the command line
# 
# So usage looks like 
#
# python day05.py ffykfhsq

from hashlib import md5
import sys

def decode_fully1(string):
    code = []
    for i in range(0, 8):
        if(i == 0):
            digit, n = decode_once1(string)
            code.append(digit)
        else:
            digit, n = decode_once1(string, n+1)
            code.append(digit)
    return code

def decode_once1(string, n=0):
    while True:
        code = encode(string + str(n))
        if(fivechars(code) == '00000'):
            return char6(code), n
        else:
            n += 1

def decode_fully2(string):
    solution = ['', '', '', '', '', '', '', '']
    n = -1
    for i in range(0, 8):
        digit, index, n = decode_digit(string, n+1, solution)
        solution[int(index)] = digit
        print(solution)
    return solution

def decode_digit(string, n, solution):
    while True:
        code = encode(string + str(n))
        if(code[:5] == '00000' and valid_char6(code[5:6], solution)):
            return code[6:7], code[5:6], n
        else:
            n += 1

def valid_char6(char6, solution):
    return char6.isdigit() and int(char6) <= 7 and solution[int(char6)] == ''
    
def encode(string):
    return md5(string.encode('utf-8')).hexdigest()

def fivechars(string):
    return string[:5]

def char6(string):
    return string[5:6]
            
if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("This script needs an input string as a", 
              "command-line argument to work")
    elif(sys.argv[2] == '1'):
        print(''.join(decode_fully1(sys.argv[1])))
    elif(sys.argv[2] == '2'):
        print(''.join(decode_fully2(sys.argv[1])))
    else:
        print("This script requires a 1 or 2 as the second",
              "command-line argument")
        

