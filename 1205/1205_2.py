import io
import sys

def surrounddec(a , b , c , d):
    decs_res = []
    decs = [c-1,d] , [c,d-1] , [c+1,d] , [c,d+1]

    for dec in decs :
        # print(dec[0] , dec[1])

        if dec[0] < 0 or dec[0] > a:
            continue
        if dec[1] < 0 or dec[1] > b:
            continue

        decs_res.append(dec)
    return(decs_res)
    



_INPUT = """\
5 7
1.2.3.4
.5.1.2.
3.4.5.1
.2.3.4.
5.1.2.3
"""
sys.stdin = io.StringIO(_INPUT)

a,b=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき

print("a : {0} b : {1}".format(a , b))

c = [[0 for i in range(a)] for j in range(b)]

for i in range(a):
    c = list(input())
    # if c == "." :
    #     c[i] = list(input())
    
        

# c[0]=list(input())
# c[1]=list(input())

print(c)

print(surrounddec(a,b,int(2),int(2)))

# for i in range(a) :
#     for j in range(b):
