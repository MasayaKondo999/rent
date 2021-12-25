import bisect

A = [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
print(A)

index = bisect.bisect_left(A, 3) # 2 最も左(前)の挿入箇所が返ってきている
#   [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
#         ^

index = bisect.bisect_right(A, 3)

index = bisect.bisect_right(A, 3) # 5
#   [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
#                  ^

# insort_left(a, x)はa.insert(bisect.bisect_left(a, x))と同じです。

