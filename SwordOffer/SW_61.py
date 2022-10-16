"""  
create in   : 2022/10/12 11:41
@author     : Psycholab.ljz 
@description:
"""

"""
从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 
0 ，可以看成任意数字。A 不能视为 14。


链接：https://leetcode.cn/leetbook/read/illustrate-lcof/e27dk2/
"""
from typing import List
list1=[0,0,1,2,5]
"""
其实没有必要搞排序，而且轻松击败100%，只要满足两个条件即可，
1，数组除0外的数最大值最小值差值必须在4以及4以内。
2. 除0以外的数保证不重复
反向思维，0既然可以代替任何数，那就别考虑它，考虑其他数，如果其他数最大最小差值大于4，那么有再多0也没用，如 1，0，0，3，6；
0既然可以代替任何值，那么无所谓，但是还要保证其他数不能重复，如0，0，1，1，3，这就不行了，
保证最大最小小于等于4，依次遍历即可（记住要除了0）
保证除0以外不重复，因为才5个数，而且5个数还有范围限制，直接来个标记数组即可，这样就轻松击败100%
代码中min初始化最低14，也可以15，。。。随便，只要不是小于扑克牌中最大值13即可，比较你要用来求最小，怕各位疑惑


"""

def isStraight( nums: List[int]) -> bool:

    nums=sorted(list1)
    jack_number=0

    for i in range(len(nums)-1):
        if nums[i]==0:
            jack_number +=1
        else:
            if nums[i]!=nums[i+1]:
                continue
            else:
                return False
    return nums[-1]-nums[jack_number] <5
print(isStraight(list1))








