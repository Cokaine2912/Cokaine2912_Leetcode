class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0 
        i = 0 
        n = len(nums)
        maxx = nums[0]
        while i < n :
            s += nums[i]
            maxx = max(maxx , s)
            if s <= 0 :
                s = 0
            i += 1

        return maxx 