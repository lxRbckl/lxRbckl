class Solution:


    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # try if (element) <
        # except then (no element) <
        try:

            c = nums.count(target)
            i = nums.index(target)

            # if (one element) <
            # elif (many element) <
            if (c == 1): return [i, i]
            elif (c > 1): return [

                i,
                (-nums[::-1].index(target) + (len(nums) - 1))

            ]

            # >

        except ValueError: return [-1, -1]

        # >
