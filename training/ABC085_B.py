import io
import sys

_INPUT = """\
9 45000
"""
sys.stdin = io.StringIO(_INPUT)

# 本番コードはこのコメント以下に書く、import,def,も

n,y=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき
y = str(y)
y = y[:-3]
y = int(y)

for m in range(y):
    

