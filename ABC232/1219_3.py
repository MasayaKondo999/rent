import io
import sys

_INPUT = """\
4 4
1 2
1 3
1 4
3 4
1 3
1 4
2 3
3 4
"""
sys.stdin = io.StringIO(_INPUT)

# 本番コードはこのコメント以下に書く、import,def,も

n,m=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき

graph_taka = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph_taka[a-1].append(b-1)
    graph_taka[b-1].append(a-1)  # 有向グラフなら消す
# print(graph_taka)  # [[2, 3, 5], ..., [1, 3, 4]]

graph_ao = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph_ao[a-1].append(b-1)
    graph_ao[b-1].append(a-1)  # 有向グラフなら消す
# print(graph_ao)  # [[2, 3, 5], ..., [1, 3, 4]]

# if graph_taka == graph_ao :

graph_ao = [ graph_ao[2] , graph_ao[1] , graph_ao[0] ,graph_ao[3]]
print(graph_ao)