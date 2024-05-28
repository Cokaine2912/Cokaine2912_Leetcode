class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        j = 0 
        n = len(nums)
        while j < n :
            while i < n and nums[i] != 0 :
                i += 1
            j = i 
            while j < n and nums[j] == 0 :
                j += 1
            if i < n and j < n and nums[i] == 0 and nums[j] != 0 :
                nums[i] , nums[j] = nums[j] , nums[i]
                i += 1
        return nums 
        