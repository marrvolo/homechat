from typing import List

def getRain(height:List[int]) -> int:
    l,r = 0, len(height)-1
    max_left = 0
    max_right = 0
    res = 0

    while r > l:
        max_left = max(height[l], max_left)
        max_right = max(height[r], max_right)

        if max_left > max_right:
            res += max_right - height[r]
            r -= 1
        else:
            res += max_left - height[l]
            l += 1
    
    return res


height = [0,1,0,2,1,0,1,3,2,1,2,1]


print(getRain(height))











