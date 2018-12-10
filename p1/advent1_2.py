#  https://adventofcode.com/2018/day/1
# add up line items, looping, until we hit a subtotal we've previously reached

import sys

data = sys.stdin.readlines()

total = 0
found = []
while 1:
    for item in data:
        total += int(item)
        if total in found:
            print "Found "+str(total)
            sys.exit()
        found.append(total)
        # print str(total)
