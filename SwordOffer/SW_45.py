"""
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。


示例 1:

输入: [10,2]
输出: "102"


输入: [3,30,34,5,9]
输出: "3033459"


提示:

0 < nums.length <= 100
说明:

输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
相关标签

Python3

# 方法1:

"""
import functools
from typing import List

num = [3, 30, 34, 5, 9]


# def minNumber(nums: List[int]) -> str:
#     num_list = list(map(str, nums))
#     print(num_list)
#     list1 = []
#
#
#     for i in range(len(nums)):
#         max = num_list[i]
#         for j in range(i + 1, len(nums)):
#             if int(num_list[i] + num_list[j]) > int(num_list[j] + num_list[i]):
#                 max = num_list[j]
#                 c = num_list[i]
#                 num_list[i] = max
#                 num_list[j] = c
#         list1.append(max)
#     return ''.join(list1)

def minNumber(nums: List[int]) -> str:
    num_list = list(map(str, nums))

    def sorted_rule(x, y):  ## 定义一个比的函数
        a = x + y
        b = y + x
        if int(a) > int(b):
            return 2  ## 如果 x>Y return 整数
        elif int(a) < int(b):
            return -1  ## 如果 x<Y return dder

    num_list = sorted(num_list, key=functools.cmp_to_key(sorted_rule))
    print(num_list)
    return ''.join(num_list)



minNumber(num)
