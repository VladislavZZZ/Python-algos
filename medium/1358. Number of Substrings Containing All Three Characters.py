class Solution:
    def has_all(self, letters):
        return len(letters.keys()) == 3

    def numberOfSubstrings(self, s: str) -> int:
        num_of_subs = 0
        letters = dict()
        left, right = 0, 0
        size = len(s)
        while right != size:
            letter = s[right]
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

            while self.has_all(letters):
                num_of_subs += size - right
                letter = s[left]
                letters[letter] -= 1
                if letters[letter] == 0:
                    del letters[letter]
                left += 1
            right += 1
        return num_of_subs


if __name__ == '__main__':
    sol = Solution()
    sol.numberOfSubstrings()