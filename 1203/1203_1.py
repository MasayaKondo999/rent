n=int(input())  #数値入力 「N」だけの入力のとき

len = len(str(n))

if n >= 42 :
    n = n + 1


if len == 1:
    print("AGC00{0}".format(n))

if len == 2:
    print("AGC0{0}".format(n))
