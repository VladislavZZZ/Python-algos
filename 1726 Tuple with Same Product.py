from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prods = dict()
        tuples_num = 0
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:]):
                prod = num1 * num2
                if prod in prods:
                    tuples_num += len(prods[prod])* 8
                    prods[prod].append((num1, num2))
                else:
                    prods[prod] = [(num1, num2)]
        return tuples_num


if __name__ == '__main__':
    sol = Solution()
    arr = [1,2,4,5,10]
    print(sol.tupleSameProduct(arr))
