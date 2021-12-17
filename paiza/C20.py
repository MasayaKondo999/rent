
m,p,q=map(float, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき

# m = float(m)

p = p / 100 

q = q /100

less = m * (1 - p)

less = less * (1 - q)

print(less)