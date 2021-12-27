import io
import sys

_INPUT = """\
4
0 1
1 3
1 1
-1 -1
"""
sys.stdin = io.StringIO(_INPUT)

# 本番コードはこのコメント以下に書く、import,def,も

import itertools

N=int(input())  #複数数値入力　「A B」みたいなスペース空いた入力のとき

plot = []

for i in range(N) :
    plot.append(list(map(int, input().split())))  #リスト入力 「a1 a2 a3 ...」みたいな配列のような入力のとき

# print(plot)
tri = []
tri = list(itertools.combinations(plot , 3))
# print(tri)
count = 0
for i in tri :
    print(i)
    # print(i[0][0])
    # print(i[1][1] , i[0][1] , i[1][0] , i[0][0] , i[2][1] , i[1][1] , i[2][0] , i[2][0])
    if (i[1][0] - i[0][0]) * (i[2][1] - i[0][1]) - (i[2][0] - i[0][0]) * (i[1][1] - i[2][1]) ==0 :
        # print(i[1][1] , i[0][1] , i[1][0] , i[0][0] , i[2][1] , i[1][1] , i[2][0] , i[2][0])
        print("同一直線上")
        
        continue

    else :
        print("三角形です  ")
        count = count + 1

print(count)