class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first_crack = False
        second_crack = False
        letter1, letter2 = "", ""
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if second_crack:
                    return False
                if not first_crack:
                    letter1 = s1[i]
                    letter2 = s2[i]
                    first_crack = True
                else:
                    if not (s1[i] == letter2 and s2[i] == letter1):
                        return False
                    second_crack = True
        if first_crack and not second_crack:
            return False
        else:
            return True
if __name__ == '__main__':
    sol = Solution()
    s1 = "siyolsdcjthwsiplccjbuceoxmpjgrauocx"
    s2 = "siyolsdcjthwsiplccpbuceoxmjjgrauocx"
    print(sol.areAlmostEqual(s1,s2))
