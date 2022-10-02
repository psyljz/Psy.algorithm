"""  
create in   : 2022/10/1 18:42
@author     : Psycholab.ljz 
@description:
"""
from typing import List

head = [1, 3, 2]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def reversePrint(self, head: ListNode) -> List[int]:

from queue import Queue
elm1 = ListNode(1)

elm2 = ListNode(2)

elm1.next = elm2

elm3 = ListNode(3)
elm4= ListNode(9)

elm2.next = elm3
elm3.next=elm4



def printfuc(Linknode):

    if Linknode.next ==None:
        print(Linknode.val)
    else:
        printfuc(Linknode.next)
        print(Linknode.val)


q =[]
def rePrintfuc(Linode):

    while(Linode!=None):
        q.append(Linode)
        Linode=Linode.next


    for i in range(len(q)-1,-1,-1):
        print(q[i].val)


rePrintfuc(elm1)
min= -1E10


