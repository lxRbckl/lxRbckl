class Solution:


    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        l = []
        for j in s:

            if (j in l): l = [*l[(l.index(j) + 1) :], j]
            else: l.append(j)

            if (len(l) > i): i = len(l)

        return i
