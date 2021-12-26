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
def indexto(n , index) :
    if index == n :
        # print(0)
        return int(0)
    else :
        # print(n - index)
        return int(n - index)

def dict_ins(dict , x , ans) :
    dict[x] = ans
    return dict

import bisect

n,q=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき

menber = []

menber=list(map(int, input().split()))  #リスト入力 「a1 a2 a3 ...」みたいな配列のような入力のとき

# menberのソート
menber.sort()

# xをlistに代入
x = [0] * q

for i in range(q) :
    x[i] = int(input())

# print(x)

# xのソート
x_sorted = sorted(x)

# print("menber = " +str(menber))
# print("x = " +str(x))
# print("x sorted = " +str(x_sorted))
men_index = 0
# findindex = n

res_dict = {}

for i in range(q) :
    for j in range(n) :
        
        if j == n - 1 :
            
            dict_ins(res_dict , x[i] , indexto(n , n))
            break
        elif menber[j] >= x[i] :
            # indexto(n , 0)
            dict_ins(res_dict , x[i] , indexto(n , 0))
            break
        elif menber[j + 1] >= x[i] :
            # indexto(n , j + 1)
            dict_ins(res_dict , x[i] , indexto(n , j + 1))
            break

# print(res_dict)
        
for i in x :
    print(res_dict[i])