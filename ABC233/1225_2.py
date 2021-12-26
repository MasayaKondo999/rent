import io
import sys

_INPUT = """\
3 7
abcdefgh
"""
sys.stdin = io.StringIO(_INPUT)

# 本番コードはこのコメント以下に書く、import,def,も

L,R=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき

S =list(input())  #数値入力 「N」だけの入力のとき

L = L -1
R = R -1

rev = S[L:R+1]

rev.reverse()

# print(rev)

if L == 0 :
    ans = rev
else :
    ans = S[0:L]
    ans = ans + rev

if len(S) == R + 1:
    # print("a")
    None
else :
    ans = ans + S[R+1:]

# print(str(ans))
print("".join(ans))