import io
import sys

_INPUT = """\
13
62
"""
sys.stdin = io.StringIO(_INPUT)

a = int(input())
b = int(input())

# print(a)
print(5000000000*b + a)