#  https://adventofcode.com/2018/day/1
# add up line items, looping, until we hit a subtotal we've previously reached

import sys

data = sys.stdin.readlines()

three = 0
two = 0

def hasthree(code):
    # sort string
    code = ''.join(sorted(code))
    chars = {}
    for c in code:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    for (a,b) in chars.items():
        if b == 3:
            return 1
    return 0

def hastwo(code):
    code = ''.join(sorted(code))
    chars = {}
    for c in code:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    for (a,b) in chars.items():
        if b == 2:
            return 1
    return 0

for item in data:
    if hasthree(item):
        three += 1
    if hastwo(item):
        two +=1

print three * two


