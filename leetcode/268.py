class Solution:


    def missingNumber(self, nums: List[int]) -> int:

        x = set(nums)
        y = set(i for i in range(max(nums) + 2))

        return sorted(list(y - x))[0]
