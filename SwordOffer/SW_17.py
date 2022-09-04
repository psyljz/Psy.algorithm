from typing import List

n = 3


## 使用字符串处理大数溢出的问题

def printNumbers(self, n: int) -> List[int]:
    list1 = []
    for i in range(10 ** n - 1):
        list1.append(i)
    return list1
