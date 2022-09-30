"""  
create in   : 2022/9/6 16:15
@author     : Psycholab.ljz 
@description: 找出数组中重复的数字出现的次数
"""
from typing import List

num_list = []

_nums = [2,2]
_target = 3


# count[ target ]numb{er appear in the nums}
# "Binary" 'Search O(log(n))

def search_range(nums: List[int], target: int) -> int:
    # 首先要找这个数 排序数组可以二分查找
    # 找到需要的数字
    low = 0  # 最小数的索引
    up = len(nums)  # 这个索引是越界的 因为后面取的整除

    midd = (low + up) // 2  # 数组最中间数的索引


    while low <= up:



        # 把目标数与数组最中间的数比较，小于中间数就上界赋给midd

        if target < nums[midd]:
            up = midd-1

        # 把目标数与数组最中间的数比较，大于于中间数就上界赋给midd
        elif target > nums[midd]:
            low = midd+1
        # 把目标数与数组最中间的数比较，等于说明找到该数 但是不确定会在重复数会有多少
        elif target == nums[midd]:
            number_count = 1

            check_index =midd
            # 首先向左检查

            while True:
                check_index -=1
                if  check_index>=0and nums[check_index]==target:
                    number_count+=1
                else:
                    break
            # 再向右检查
            check_index = midd
            while True:
                check_index +=1
                if check_index<len(nums) and nums[check_index]==target:
                    number_count+=1
                else:
                    break

            # 算法结束返回 索引
            return number_count
        midd = (low + up) // 2  # 数组最中间数的索引

        if midd >=len(nums):
            return 0



print(search_range(_nums, _target))
