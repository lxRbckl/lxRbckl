from itertools import combinations


class Solution:


    def twoSum(self, nums: List[int], target: int) -> List[int]:

        x, y = list(filter(lambda i : sum(i) == target, combinations(nums, 2)))[0]
        return [

            nums.index(x),
            ((-nums[::-1].index(y)) + (len(nums) - 1))

        ]
