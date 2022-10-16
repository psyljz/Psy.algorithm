"""  
create in   : 2022/10/5 10:04
@author     : Psycholab.ljz 
@description: 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

力扣 SW_59: https://leetcode.cn/leetbook/read/illustrate-lcof/5iy0oi/

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

思路一:

    1.遍历数组把最大值存入队列中 O(n*k)
    2.FIFO输出队列

思路一:




"""
nums = [-7, -8, 7, 5, 7, 1, 6, 0]
k = 4
from collections import deque

"""

思路三：
时间复杂度

"""
from typing import List

from collections import deque

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    ## 设定一个滑动的窗口

    start_index = 1 - k
    k_index = 0
    if k == 1:
        return nums
    result = []
    que = deque()

    ## 当kindex指向数组最后一位时结束循环
    while k_index < len(nums):
        ## 左指针小于0时窗口没有完全进入数组
        if len(que) != 0:

            if start_index >= 0:
                if que[0] == nums[start_index - 1]:
                    que.popleft()
            if que[-1] <= nums[k_index]:
                que.pop()
                while (True):
                    if len(que) == 0 or que[-1] >= nums[k_index]:
                        que.append(nums[k_index])
                        break
                    que.pop()
            else:
                que.append(nums[k_index])


        else:
            que.append(nums[k_index])

        if start_index >= 0:
            result.append(que[0])

        start_index += 1
        k_index += 1
    print(result)
    return result


maxSlidingWindow(nums, k)

"""



思路一：
时间复杂度

"""

# from typing import List
#
#
# def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
#     ## 设定一个滑动的窗口
#
#     start_index = 0
#     k_index = k
#     result =[]
#
#     # 当窗口的index小于数组的长度时进行循环
#     while (k_index <= len(nums)):
#         result.append(max(nums[start_index:k_index]))
#         start_index += 1
#         k_index += 1
#     return result
#
# maxSlidingWindow(nums, k)


"""

思路二：
时间复杂度

"""

from typing import List

# def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
#     ## 设定一个滑动的窗口
#
#     start_index = 0
#     k_index = k
#     result =[]
#     stack=[]
#     if k ==1:
#         return nums
#
#
#     # 使用辅助栈
#
#     while (k_index <= len(nums)):
#
#         if len(result)!=0:
#             ## 如果向前滑动的数在辅助栈内
#             if stack[0]==nums[start_index-1]:
#                 stack.pop(0)
#             if len(stack)!=0:
#                 if stack[-1]>nums[k_index-1]:
#                     result.append(stack[-1])
#                 else:
#                     result.append(nums[k_index-1])
#                     stack.append(nums[k_index-1])
#             else:
#                 result.append(max(nums[start_index:k_index]))
#                 stack.append(max(nums[start_index:k_index]))
#             start_index += 1
#             k_index += 1
#
#         else:
#             result.append(max(nums[start_index:k_index]))
#             stack.append(max(nums[start_index:k_index]))
#             start_index += 1
#             k_index+=1
#     print(result)
