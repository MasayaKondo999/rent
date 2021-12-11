

# 本番コードはこのコメント以下に書く、importも

import bisect

A = [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]

print(A)
print("")
index =  bisect.bisect_left(A, 9) 
print(index)
A.insert(index, 9)

print(A) # [1, 2, 3, 3, 3, 3, 4, 4, 6, 6, 6, 6]