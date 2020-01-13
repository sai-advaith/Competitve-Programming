class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
                    decom = []
                    for i in range(len(nums)//2):
                            decom.extend([nums[2*i+1]]*nums[2*i])
                    return decom