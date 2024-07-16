class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in nums:
            j = abs(i)
            if nums[j] < 0:
                return j
            nums[j] = -nums[j]