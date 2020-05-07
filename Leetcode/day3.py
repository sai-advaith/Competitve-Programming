class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        summation = current_sum
        for i in range(1,len(nums)):
            current_sum = max(current_sum+nums[i],nums[i])
            summation = max(current_sum,summation)
        return summation