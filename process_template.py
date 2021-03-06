#二次配列をfor文で回す 
AX = [[0,0] , [0,1] , [0,2] , [0,3] , [1,0] , [1,2]]

for x,i in AX:
    print(x , i)

# listのスライス
l = [0, 10, 20, 30, 40, 50, 60]

print(l[:3])
# [0, 10, 20]

print(l[::2]) #stepを指定している、stepは要素の間隔を指定して取得する方法
# [0, 20, 40, 60] #偶数個目の要素のみ

# 配列を要素ごとに改行する
print(*l,sep="\n")

# list を反転
l.reverse()

# 二次配列以上、特定の行、列でソート
AX = sorted(AX, reverse=True , key=lambda x: x[0])
print("二次配列以上、特定の行、列でソート" + str(AX))