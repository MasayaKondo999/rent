import io
import sys

_INPUT = """\
abc
ijk
"""
sys.stdin = io.StringIO(_INPUT)

# 本番コードはこのコメント以下に書く、import,def,も

def zurasu(str , int) :
    tb = ord(str)
    tb = tb + int

    if tb >= 123 :
        return(chr(tb - 26))
    
    elif tb <= 96 :
        return(chr(tb + 26))

    else :
        return(chr(tb))

s = str(input())
t = str(input())

s = list(s)
t = list(t)

len = len(s)

flag = 0

diff = ord(t[0]) - ord(s[0])  
# print(diff)
for i in range(len) :
    # print (t[i] , ord(t[i]) , s[i]  , ord(s[i]), diff)
    if zurasu(s[i] , diff) == t[i]:
        continue
    else :
        flag = 1
        break

# for i in range(26) :
    
#     for j in range(len) :

#         if

if flag == 1 :
    print("No")
else :
    print("Yes")

# print(zurasu("z" , 24))