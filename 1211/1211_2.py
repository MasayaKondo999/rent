import io
import sys


_INPUT = """\
6
snuke
snuke
takahashi
takahashi
takahashi
aiai
"""
sys.stdin = io.StringIO(_INPUT)

import collections

n = int(input())
low = []

for i in range(n) :
    low.append(input())

c = collections.Counter(low)
# print(c)

print(c.most_common()[0][0])