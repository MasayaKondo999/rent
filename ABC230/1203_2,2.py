s=(input()) 

flag = False #no

# arr = []
# for i in s:
#     arr.append(i)

# print(arr)
len = len(str(s))

sam1 = 'oxxoxxoxxoxxoxx'
sam2 = 'xxoxxoxxoxxoxx'
sam3 = 'xoxxoxxoxxoxx'

result = s in sam1
# print(result)
flag = result

# result = s in sam2

if flag :
    print("Yes")
else:
    print("No")