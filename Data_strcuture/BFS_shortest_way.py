"""  
create in   : 2022/9/23 17:50
@author     : Psycholab.ljz 
@description:
"""
"""  
create in   : 2022/9/22 11:18
@author     : Psycholab.ljz 
@description:用邻接矩阵储存图，然后用BFS遍历
"""

from queue import Queue  # FIFO

# 定义一个FIFO的队列
q1 = Queue()

# 定义一个图
# graph = [
#     [0, 1, 1, 0, 0, 1, 1],
#     [1, 0, 1, 1, 0, 0, 0],
#     [1, 1, 0, 0, 0, 0, 1],
#     [0, 1, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 1, 0, 0, 0],
#     [1, 0, 1, 0, 0, 0, 0],
# ]

graph = [
    [0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],

]

node_list = ["A", "B", "C", "D","E","F","G"]
visited = [0, 0, 0, 0,0,0,0]


def BFS(node):

    visit_n(node)
    visited[node] = 1
    while not q1.empty():
        x = q1.get()
        if visited[x] == 0:
            visit_n(x)


def visit_n(node):
    visited[node] = 1
    print(node_list[node])
    
    for i in range(len(graph[node])):
        if graph[node][i] == 1 and visited[i] == 0:
            q1.put(i)
        else:
            continue

sart_node= 0

BFS(sart_node)

for i in range(len(visited)):

    if visited[i] == 0:
        # print(i)
        BFS(i)
print(visited)