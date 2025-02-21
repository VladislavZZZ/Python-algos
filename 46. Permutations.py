from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        permutations = []
        for _ in range(len(nums)):
            n = nums.pop(0)
            sub_perms = self.permute(nums)

            for p in sub_perms:
                p.append(n)

            permutations.extend(sub_perms)
            nums.append(n)

        return permutations


if __name__ == '__main__':
    nums = [1,2,3]
    s = Solution()
    a = s.permute(nums)
    print(a)