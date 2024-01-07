class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        
        i = 0
        j = 1
        n = len(nums)
        ans = 0
        while j < n :
            if nums[j] > nums[i] :
                profit = nums[j] - nums[i]
                ans = max(profit,ans)
            else :
                i = j
            j += 1
        return ans 