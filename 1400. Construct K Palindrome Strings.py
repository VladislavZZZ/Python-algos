# Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

# Constraints:
#
# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= 105
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        frq_letters = dict()
        lonely_letter_count = 0
        for letter in s:
            if letter in frq_letters:
                frq_letters[letter] += 1
                if frq_letters[letter] % 2 == 0:
                    lonely_letter_count -= 1
                else:
                    lonely_letter_count += 1
            else:
                frq_letters[letter] = 1
                lonely_letter_count += 1

        return k <= len(s) or k >= lonely_letter_count


if __name__ == '__main__':
    sol = Solution()
    s = "annabelle"
    k = 2
    print(sol.canConstruct(s, k))
