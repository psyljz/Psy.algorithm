"""  
create in   : 2022/10/2 10:56
@author     : Psycholab.ljz 
@description:
"""
from typing import List

pushed = [4,0,1,2,3]

popped = [4,2,3,0,1]





def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:

    if len(pushed)==0:
        return True
    ## 建立一个辅助栈
    stack = []

    ## 入栈指针
    push_index = 0

    ## 出栈指针
    pop_index = 0

    # 对入栈顺序进行遍历
    while push_index < len(pushed):  # range[0,len(List:pushed) )
        # 如果入栈指针和出栈指针指向的值相等说明为下一个出栈的元素
        if pushed[push_index] == popped[pop_index]:
            pop_index += 1
            push_index += 1
        # 如果入栈指针和出栈指针指向的值不相等说明该元素先入栈
        elif pushed[push_index] != popped[pop_index]:
            ## 如果辅助不为空 检查辅助栈的最有一个元素能否出栈
            if len(stack)!=0:
                if stack[-1] == popped[pop_index]:
                    stack.pop()
                    pop_index+=1
                    continue
            stack.append(pushed[push_index])
            push_index += 1

    if len(stack) == len(popped[pop_index:]):
        while (pop_index < len(pushed)):
            if popped[pop_index] == stack[-1]:
                stack.pop(-1)
            pop_index+=1
    if len(stack)==0:
        return True
    return False


print(validateStackSequences(pushed,popped))