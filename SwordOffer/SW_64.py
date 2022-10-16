"""  
create in   : 2022/10/5 11:19
@author     : Psycholab.ljz 
@description:
"""


def sumNums( n: int) -> int:
    if n == 1 or n == 0:
        return n
    else:
        return sumNums(n - 1)  +n

print(sumNums(5))