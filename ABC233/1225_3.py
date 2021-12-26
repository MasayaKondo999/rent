import io
import sys

_INPUT = """\
2 40
3 1 8 4
2 10 5
"""
sys.stdin = io.StringIO(_INPUT)

# 本番コードはこのコメント以下に書く、import,def,も

N,X=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき

ball = [0] * N

for i in range(N) :
    temp =list(map(int, input().split()))
    # print(temp)
    roop = temp[0]
    for j in range(roop) :
        ball[i] = temp[1:]

print(ball)

ball_num = len(ball)
# print(ball_num)
for i in ball :
    # print(i)
    for j in i :
        # print(j)

        print(j)