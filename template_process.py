n=int(input())  #数値入力 「N」だけの入力のとき

a,b=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき

c=list(map(int, input().split()))  #リスト入力 「a1 a2 a3 ...」みたいな配列のような入力のとき

s=[list(map(int,list(input()))) for i in range(h)]  # 二次元配列入力　二次元マップみたいな入力のとき
