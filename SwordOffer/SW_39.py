"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。



你可以假设数组是非空的，并且给定的数组总是存在多数元素。



输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2


限制：

1 <= 数组长度 <= 50000



## 方法一 排序后 中间的数即为答案
## 方法 hashmap存 统计超过一半的数就为答案
## 方法三 摩尔投票

"""

kus = [1, 2, 3, 2, 2, 2, 4, 2, 22, 2, 2,211,44]
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = 0
        count = 0

        for i in nums:

            if count == 0:
                cur = i
            if cur==i:
                count+=1
            else:
                count-=1
        return cur

new =Solution()
print(new.majorityElement(kus))



