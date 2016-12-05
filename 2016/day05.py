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
# ----------------------------------------------------------------------------
#
# To run this script, you need to input the text string on the command line
# 
# So usage looks like 
#
# python day05.py ffykfhsq

from hashlib import md5
import sys

def decode_fully(string):
    code = []
    for i in range(0, 8):
        if(i == 0):
            digit, n = decode_once(string)
            code.append(digit)
        else:
            digit, n = decode_once(string, n+1)
            code.append(digit)
    return code

def decode_once(string, n=0):
    while True:
        code = encode(string + str(n))
        if(fivechars(code) == '00000'):
            return char6(code), n
        else:
            n += 1

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
    else:
        print(''.join(decode_fully(sys.argv[1])))

