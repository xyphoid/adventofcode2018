#  https://adventofcode.com/2018/day/1
# add up all line items in stdin

import sys

data = sys.stdin.readlines()

total = 0
for item in data:
    total += int(item)
print total