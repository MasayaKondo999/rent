x,y=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき


if x >= y :
    print(0)

else :
    less = y - x 
    print(-(- less // 10 ))