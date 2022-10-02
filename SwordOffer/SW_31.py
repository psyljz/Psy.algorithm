"""  
create in   : 2022/10/2 10:56
@author     : Psycholab.ljz 
@description:
"""
from typing import List

pushed = [2,1,0]

popped = [1,2,0]




def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:

    stack = []
    # 模拟？什么叫模拟？
    pushed_index = 0
    popped_index = 0
    while (pushed_index < len(pushed)):
        # 如果出栈中的数字与入栈中的数不相等 则 把入栈序列中的数放入辅助栈中 且入栈的index加1
        if pushed[pushed_index] != popped[popped_index]:
            stack.append(pushed[pushed_index])
            pushed_index += 1
        # 如果出栈中的数字与入栈中的数相等 则 把该入栈序列中的数放入辅助栈后 再删除该元素 辅助栈加入该元素再删除该元素  入栈index加1 出栈index加1
        elif pushed[pushed_index] == popped[popped_index]:
            pushed_index += 1
            popped_index += 1

    while (popped_index < len(pushed)):
        if popped[popped_index] == stack[-1]:
            stack.pop(-1)
        popped_index+=1

    while(len(stack)>0):

        if stack[-1] == popped[popped_index]:
            stack.pop()
            popped_index +=1


    if len(stack)==0:
        return True
    return False

print(validateStackSequences(pushed,popped))