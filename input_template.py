import io
import sys

_INPUT = """\
2
1 2 3
aaa
"""
sys.stdin = io.StringIO(_INPUT)

# 本番コードはこのコメント以下に書く、import,def,も


n = int(input())
a , b , c = list(map(int, input().split()))

print(n)

print(a , b , c)

print(list(input()))

# テスト出力
# 2
# [1, 2, 3]
# ['a', 'a', 'a']