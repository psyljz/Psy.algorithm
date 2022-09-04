from typing import List

_numbers =[54,88,99,1, 2, 3, 4, 5,6,7,8,9,9,9,9]

## 二分查找


def minArray(numbers: List[int]) -> int:
    right = len(numbers)-1
    left = 0
    while True:
        mid = (right+left)//2

        if right ==left:
            return numbers[left]
        if numbers[right] >numbers[mid]:
            right =mid
        elif numbers[right] <numbers[mid]:
            left=mid+1
        elif numbers[right]==numbers[mid]:
            right =right-1

print(minArray(_numbers))





