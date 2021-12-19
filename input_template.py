n=int(input())  #数値入力 「N」だけの入力のとき

a,b=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき

c=list(map(int, input().split()))  #リスト入力 「a1 a2 a3 ...」みたいな配列のような入力のとき

s=[list(map(int,list(input()))) for i in range(h)]  # 二次元配列入力　二次元マップみたいな入力のとき

# 最初にすべて読み込む必要がある場合 - 事前に各リストを用意しておく
N = int(input())

t = [0] * N
x = [0] * N

for i in range(N):
    t[i] , x[i] = map(int, input().split())

