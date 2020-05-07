class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = len(nums)
        n = nums.count(0)
        nums.extend([0]*n)
        for i in range(k):
            if (len(nums) == k):
                return nums
            else:
                if nums[i] == 0:
                    nums.remove(0)