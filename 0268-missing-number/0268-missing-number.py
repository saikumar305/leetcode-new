class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i

        n = len(nums) + 1
        return (n*(n-1) // 2) - sum(nums)
        