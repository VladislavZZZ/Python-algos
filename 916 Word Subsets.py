# You are given two string arrays words1 and words2.
# A string b is a subset of string a if every letter in b occurs in a including multiplicity.
#
# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.
#
# Return an array of all the universal strings in words1.You may return the answer in any order.
#
# Example
# 1:
#
# Input: words1 = ["amazon", "apple", "facebook", "google", "leetcode"], words2 = ["e", "o"]
# Output: ["facebook", "google", "leetcode"]
# Example
# 2:
#
# Input: words1 = ["amazon", "apple", "facebook", "google", "leetcode"], words2 = ["l", "e"]
# Output: ["apple", "google", "leetcode"]
#
# Constraints:
#
# 1 <= words1.length, words2.length <= 104
# 1 <= words1[i].length, words2[i].length <= 10
# words1[i] and words2[i] consist only of lowercase English letters.
# All the strings of words1 are unique.


import re


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        res = []
        letter_freq = dict()
        temp_freq = dict()
        for word in words2:
            for letter in word:
                if letter in temp_freq:
                    temp_freq[letter] += 1
                else:
                    temp_freq[letter] = 1
            for (k,val) in temp_freq.items():
                if k in letter_freq:
                    letter_freq[k] = max(val, letter_freq[k])
                else:
                    letter_freq[k] = val
            temp_freq= dict()
        temp_freq = dict()
        for word in words1:
            for letter in word:
                if letter in temp_freq:
                    temp_freq[letter]+= 1
                else:
                    temp_freq[letter] = 1
            is_universal = True
            for (k,val) in letter_freq.items():
                if k not in temp_freq:
                    is_universal =False
                    break
                elif val > temp_freq[k]:
                    is_universal = False
                    break
            if is_universal:
                res.append(word)
            temp_freq = dict()
        return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["lo","eo"]
    res = sol.wordSubsets(words1, words2)
    print(res)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
