#  https://adventofcode.com/2018/day/2
# locate two lines with almost-identical sets

import sys

data = sys.stdin.readlines()


for line1 in data:
    for line2 in data:
        diffs = 0;
        for i, c in enumerate(line1):
            if(c != line2[i]):
                diffs += 1
        if diffs == 1:
            print line1
            print line2