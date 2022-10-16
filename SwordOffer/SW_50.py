"""  
create in   : 2022/10/12 11:27
@author     : Psycholab.ljz 
@description:
"""
ss =""
def firstUniqChar( s: str) -> str:
    #只出现一次：要遍历全部字符串 时间复杂度 O(n)
    # 用字典存下来 空间复杂度 O(n)
    res_dict ={}
    for i in s:
        if i not in res_dict.keys():
            res_dict[i] = 1
        else:
            res_dict[i] =res_dict[i]+1

    for k,v in res_dict.items():
        if v==1:
            return k
    return " "

print(firstUniqChar(ss))
