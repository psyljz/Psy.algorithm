"""  
create in   : 2022/10/8 11:11
@author     : Psycholab.ljz 
@description:
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。


链接：https://leetcode.cn/leetbook/read/illustrate-lcof/504usr/

"""
# target = 9
# [[2,3,4],[4,5]]

from typing import List


def findContinuousSequence(target: int) -> List[List[int]]:
    left_index = target - 2
    right_index = target - 1

    res =[]


    while(left_index>=0):
        new_list=list(range(left_index,right_index+1))
        sum2 = (left_index + right_index) * (right_index - left_index + 1) / 2
        if sum2>target:
            left_index -=1
            right_index-=1
        if sum2<target:
            left_index -=1
        if sum2 == target:
            res.insert(0,new_list.copy())
            left_index -=1
            right_index-=1
        new_list.clear()

    return res


print(findContinuousSequence(15))
