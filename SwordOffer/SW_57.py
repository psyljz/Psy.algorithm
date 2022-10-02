"""  
create in   : 2022/10/1 18:13
@author     : Psycholab.ljz 
@description:
"""
from typing import List

num_list = [2,7,11,15]

def twoSum(nums: List[int], target: int) -> List[int]:

    ## 在一个递增排序的数组中找到两个数字相加等于target
    ## 双指针
    font = 0
    end = len(nums) - 1
    while (font<end):
        ## 在一个递增排序的数组中找到两个数字大于target
        if nums[font]+nums[end] > target:
            end -= 1
        elif nums[font] + nums[end] < target:
            font += 1
        else:
            return [nums[font],nums[end]]

    return []

print(twoSum(num_list,9))











