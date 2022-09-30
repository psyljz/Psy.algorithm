"""  
create in   : 2022/9/23 16:52
@author     : Psycholab.ljz 
@description: 用邻接矩阵储存图，然后用DFS遍历
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

node_list = ["A", "B", "C", "D", "E", "F", "G"]
visited = [0, 0, 0, 0, 0, 0, 0]


def visit_node(node):

    if visited[node]!=1:  ##如果这个节点没有被访问过
        print(node_list[node])
        visited[node]=1

        for i in range(len(graph[node])):
            if graph[node][i] == 1 and visited[i] != 1:
                visit_node(i)




visit_node(0)
