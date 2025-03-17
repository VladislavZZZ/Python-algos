from typing import List


def divideArray(nums: List[int]) -> bool:
    pairs_map = set()
    for num in nums:
        if num in pairs_map:
            pairs_map.remove(num)
        else:
            pairs_map.add(num)

    if len(pairs_map) > 0:
        return False
    else:
        return True


class Solution:
    pass

