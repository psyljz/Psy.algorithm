"""  
create in   : 2022/9/30 18:16
@author     : Psycholab.ljz 
@description:
"""
from typing import List

num_list = [1]


def missingNumber( nums: List[int]):

    ## 递增数组中 索引对应这值
    ## 二分查找

    left =0
    right =len(nums)

    mid= (left+right) // 2

    while True:
        if nums[mid] == mid:
            left = mid +1
        elif nums[mid] !=mid:
            right= mid
        mid = (left + right) // 2

        if left==right:
            return right


print(missingNumber(num_list))



