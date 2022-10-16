"""  
create in   : 2022/10/12 11:36
@author     : Psycholab.ljz 
@description:
"""

"""字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。


链接：https://leetcode.cn/leetbook/read/illustrate-lcof/59rlj7/
"""

s = "abcdefg"
k = 2

def reverseLeftWords(s: str, n: int) -> str:
    return s[n:]+s[:n]


print(reverseLeftWords(s,k))