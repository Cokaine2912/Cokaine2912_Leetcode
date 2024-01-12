class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        zero = 0 
        i = 0 
        j = 0
        n = len(nums)
        while j < n and zero <= 1 :
    
            if nums[j] == 0 and zero < 1 :
                zero += 1
            j += 1
    
            ans = max(ans,j-i-1)

            while i < n and j < n and nums[j] == 0 and zero == 1:
                while i < n and nums[i] == 1 :
                     i += 1
       
                if nums[i] == 0 :
                    i += 1
                    zero -= 1

        return ans


        