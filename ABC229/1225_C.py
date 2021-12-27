import io
import sys

_INPUT = """\
3 5
3 1
4 2
2 3
"""
sys.stdin = io.StringIO(_INPUT)

# 本番コードはこのコメント以下に書く、import,def,も


N,W=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき

# Wはチーズの限界
chee = []
for i in range(N) :
    chee.append(list(map(int, input().split())))

# print(chee)

chee = sorted(chee, reverse=True , key=lambda x: x[0])

# print(chee)
chee_n = 0
uma = 0
while W >= 0 :
    if W >= chee[chee_n][1] : #チーズまだ全部使える
        uma = uma + chee[chee_n][1] * chee[chee_n][0]
        W = W - chee[chee_n][1]
        chee_n = chee_n + 1
    else :
        uma = uma + W * chee[chee_n][0]
        break
    if chee_n == len(chee) :
        break

print(uma)
