s=(input()) 

arr = []
for i in s:
    arr.append(i)

# print(arr)
len = len(str(s))



# print(len)
index = 999

for i in range(len):
    
    if len == 2 :
        flag = 0
        break

    if index == 999:
        flag = 1

    # 初期値
    if index == 999 :
        if arr[i] == "o":
            index = i
            # print("index " + str(index))

    # index読み込み後
    else :
        if arr[i] == "o":
            diff = i - index
            if diff % 3 == 0 :
                # okke-
                flag = int(0)
                continue
            else :
                # dame
                flag =int(1)
                # print("No")
                break
        else : # arr [i] != 0 つまり　= "x"
            diff = i - index
            if diff % 3 == 0 :
                # no
                flag = int(1)
                break
            else :
                # yes
                flag =int(0)
                # print("No")
                continue

if flag == 1 :
    print("No")
else:
    print("Yes")




    
    # print(i)
    # print(index)
    
