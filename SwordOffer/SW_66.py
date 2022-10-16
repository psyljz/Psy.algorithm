"""  
create in   : 2022/10/12 12:10
@author     : Psycholab.ljz 
@description:
"""
"""
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
from typing import List


inpu2t=[1,2,3,4,5]


## 暴力解法

# def constructArr( a: List[int]) -> List[int]:
#
#     res =[]
#     for i in range(len(a)):
#         newlist=a.copy()
#         newlist.pop(i)
#         sum2 =1
#
#         for i in newlist:
#             sum2 =i*sum2
#
#         res.append(sum2)
#     return res


def constructArr( a: List[int]) -> List[int]:
    ##减少时间复杂度分成2个三角区计算
    res=[1]*len(a)
    sum=1
    for i in range(0,len(a)-1):

        sum=a[i]*sum
        res[i+1]=sum

    sum=1
    for x in range(len(a)-2,-1,-1):

        sum=a[x+1]*sum
        res[x]=sum*res[x]
    return res


print(constructArr(inpu2t))