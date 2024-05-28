class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        j = 0 
        n = len(nums)
        while j < len(nums) :
            while j < len(nums) and nums[i] == nums[j] :
                j += 1

            if i + 1 < n and j < n and nums[i] != nums[j] and j - i >= 2 :
                nums[i + 1] = nums[j]
                i += 1
            else :
                i += 1
            # print(nums)
        return i
            
        