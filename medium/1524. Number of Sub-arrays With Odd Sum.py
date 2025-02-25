from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        limit = 1e9 + 7
        dp_even, dp_odd = [0] * n, [0] * n
        arr_clear = [el % 2 for el in arr]
        if arr_clear[n - 1] == 0:
            dp_even[n - 1] = 1
        else:
            dp_odd[n - 1] = 1

        for num in range(n - 2, -1, -1):
            if arr_clear[num] == 1:
                dp_odd[num] = 1 + dp_even[num + 1]
                dp_even[num] = dp_odd[num + 1]
            else:
                dp_even[num] = 1 + dp_even[num + 1]
                dp_odd[num] = dp_odd[num + 1]
        count = 0
        for odd_count in dp_odd:
            count += odd_count
        count %= limit

        return int(count)


if __name__ == '__main__':
    sol = Solution()
    arr = [2,4,6]
    numOfSubarrays = sol.numOfSubarrays(arr)
    print(numOfSubarrays)
