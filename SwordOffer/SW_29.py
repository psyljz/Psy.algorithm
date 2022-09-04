"""
输入：matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]
输出：[1,2,3,6,9,8,7,4,5]


输入：matrix = [
[1,2,3,4,8,0],
[1,2,3,4,8,0],
[1,2,3,4,8,0],
[1,2,3,4,8,0],
[1,2,3,4,8,0],
[1,2,3,4,8,0],
]

输出：[1,2,3,4,8,12,11,10,9,5,6,7]


#方法1:
col =0
row =0


"""

list2 = [
[1,2,3,4,8,0],
[1,2,3,4,8,0],
[1,88,3,4,8,0],
[1,2,127257,4,8,0],
[1,2,3,4,8,0],
[1,2,3,4,8,0],


]

from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if len(matrix) == 0:
        return []
    list1 = []
    left = 0
    right = len(matrix[0]) - 1
    down = len(matrix) - 1
    up = 0

    while True:

        if left > right:
            break

        # 首先从左到右遍历
        for i in range(left, right + 1):
            list1.append(matrix[up][i])
        up = up + 1

        # 首先从上到到下遍历
        for i in range(up, down + 1):
            list1.append(matrix[i][right])
        right = right - 1
        if up > down:
            break
        # 首先从右到左遍历
        if left > right:
            break
        for i in range(right, left - 1, -1):
            list1.append(matrix[down][i])
        down = down - 1

        if up > down:
            break

        # 首先从上向上遍历
        for i in range(down, up - 1, -1):
            list1.append(matrix[i][left])
        left = left + 1
    return list1




print(spiralOrder(list2))
