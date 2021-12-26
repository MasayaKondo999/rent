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

N,Q=map(int,input().split())
A=[(a,10**9) for a in map(int,input().split())]
X=[]


for i in range(Q):
  x=int(input())
  X.append((x,i))

AX=sorted(A+X)[::-1]

# print("sorted AX:" + str(AX))

ans=[0]*Q
cnt=0

for x,i in AX:
  if i<Q:
    ans[i]=cnt
  else:
    cnt+=1

print(*ans,sep="\n")
# print(ans,sep="\n")