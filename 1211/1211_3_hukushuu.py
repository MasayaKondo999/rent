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

# 本番コードはこのコメント以下に書く、import,def,も

import bisect

n ,q=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき

A = list(map(int, input().split())) 
A = sorted(A)



    # for i in range(q) :
    #     X = int(input())
    #     index = bisect.bisect_left(A , X)
    #     print( n - index )
# print(X)


X = [0]*q
for i in range(q) :
    X[i] = int(input())

for i in range(q) :
    index = bisect.bisect_left(A , X[i])
    print( n - index )
