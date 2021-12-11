import io
import sys

_INPUT = """\
5 5
1 2 3 4 5
6
5
4
3
2
"""
sys.stdin = io.StringIO(_INPUT)

# 本番コードはこのコメント以下に書く、importも

import bisect

n,q=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき

menber = []

menber=list(map(int, input().split()))  #リスト入力 「a1 a2 a3 ...」みたいな配列のような入力のとき

# menber = sorted(menber)
menber.sort()

# xのループ
for i in range(q) :
    x = int(input())

    for j in range(n) :
        findindex = n
        
        findindex = bisect.bisect_left(menber,x)


    if findindex == n :
        print(0)
    else :
        print(n - findindex)
