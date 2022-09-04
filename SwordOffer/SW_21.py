from typing import List

_nums =[1,2,3,4,4,5,6,3,5]


## 双指针


def exchange(nums: List[int]) -> List[int]:
    start = 0
    end = len(nums) - 1

    while start < end:
        while start < len(nums) - 1:
            if nums[start] % 2 == 0:
                break
            start += 1

        while end >= 0:
            if nums[end] % 2 == 1:
                break
            end -= 1
        if start > end:
            break
        x = nums[start]

        nums[start] = nums[end]
        nums[end] = x
    print(nums)
    return nums



exchange(_nums)