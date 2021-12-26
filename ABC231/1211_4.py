from _typeshed import SupportsLenAndGetItem
import io
import sys

_INPUT = """\
4 2
1 3
2 3
"""
sys.stdin = io.StringIO(_INPUT)

# 本番コードはこのコメント以下に書く、importも

n,m=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき

for _ in range(m) :
    A ,B =map(int, input().split()) 