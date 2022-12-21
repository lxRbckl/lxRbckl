from math import log, ceil, floor


class Solution:


    def isPowerOfTwo(self, n: int) -> bool:

        if (n <= 0): return False
        elif (n == 1): return True
        elif (n >= 2):

            var = (log10(n) / log10(2))
            return ceil(var) == floor(var)
