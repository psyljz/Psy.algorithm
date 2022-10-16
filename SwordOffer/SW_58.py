"""  
create in   : 2022/10/8 11:35
@author     : Psycholab.ljz 
@description:
"""

dd="today is     great a day"
def reverseWords( s: str) -> str:


    tmp=[]
    res =[]
    for i in s:
        if i != " ":
            tmp.append(i)
        elif i == " " and len(tmp)!=0:
            res.append("".join(tmp.copy()))
            tmp.clear()
    return " ".join(res[::-1])

print(reverseWords(dd))


