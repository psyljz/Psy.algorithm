"""  
create in   : 2022/10/8 16:28
@author     : Psycholab.ljz 
@description:
"""

from typing import List

nums =[1, 0, 1, 4, 2, 5, 3]


# def findRepeatNumber(nums: List[int]) -> int:
#     set_list = set()
#     for i in range(len(nums)):
#
#         set_list.add(nums[i])
#
#         if i>=len(set_list):
#             return nums[

def findRepeatNumber(nums: List[int]) -> int:

    for i in range(len(nums)):
        #如果当前坐标不是相应的坐标
        if nums[i]!=i:
            #当前坐标交换到相应的坐标上
            if nums[nums[i]] !=nums[i]:
                temp = nums[i]
                nums[i] =nums[nums[i]]
                nums[temp] = temp
                if nums[i] != i:
                    if nums[nums[i]] ==nums[i]:
                        return nums[i]
            elif nums[nums[i]] ==nums[i]:
                return nums[i]

print(findRepeatNumber(nums))









