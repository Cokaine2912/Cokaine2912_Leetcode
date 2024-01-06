class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        i = 0 
        count = 0
        ans = 0
        while i < len(nums) :
            if nums[i] == 1 :
                count += 1
                ans = max(ans,count)
            elif nums[i] == 0 :
                count = 0
            i += 1

        return ans

        