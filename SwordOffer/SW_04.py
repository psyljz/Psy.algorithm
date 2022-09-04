"""
题目描述 https://leetcode.cn/leetbook/read/illustrate-lcof/xz2hh7/
题目描述
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例：

现有矩阵 matrix 如下：


[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

给定 target = 5，返回 true。

限制：

0 <= n <= 1000

0 <= m <= 1000

作者：画手大鹏
链接：https://leetcode.cn/leetbook/read/illustrate-lcof/xz2hh7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
from typing import List

_matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
    [18, 21, 23, 26, 30],
    [18, 21, 23, 26, 30],
    [18, 21, 23, 26, 30],
]


class Solution:

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        row_num_begin = len(matrix) - 1
        colum_begin = 0

        while ((row_num_begin >=0 and colum_begin <= len(matrix[0]) - 1)):

            if target == matrix[row_num_begin][colum_begin]:
                return True
            elif target < matrix[row_num_begin][colum_begin]:
                row_num_begin -= 1
            elif target > matrix[row_num_begin][colum_begin]:
                colum_begin += 1
        return False

"""
总结:
    1.数组越界问题要注意 数组下标变化的方向 而不是单一注意上届
"""
