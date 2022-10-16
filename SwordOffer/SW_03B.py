"""  
create in   : 2022/10/8 17:15
@author     : Psycholab.ljz 
@description:
"""

from typing import List

eode = "pwwkew"


def lengthOfLongestSubstring(s: str) -> int:

    ### 清晰的写下思路
    ## 定义2个指针
    start_index=0
    end_index=0
    dict_table={}
    best =0

    while end_index<len(s):
        if s[end_index] not in dict_table.keys():
            dict_table[s[end_index]]=end_index+1

        else:

            if best < end_index - start_index:
                best = end_index -start_index
            dict_table[s[end_index]] = end_index+1
            start_index = dict_table[s[end_index]]


        end_index+=1
    return max(end_index -start_index,best)

print(lengthOfLongestSubstring(eode))


