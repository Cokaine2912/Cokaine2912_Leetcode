class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0 
        j = 0 
        n = len(nums)
        maxx = 0
        zeros  = 0 
        while j < n :
            while zeros <= k and j < n :
                if nums[j] == 0 :
                    zeros += 1
                j += 1
            if zeros == k + 1 :
                maxx = max(j-i-1 , maxx)
                while nums[i] != 0 :
                    i += 1
                if nums[i] == 0 :
                    zeros -= 1 
                    i += 1
            elif zeros <= k  :
                maxx = max(j-i,maxx)
            # print(i,j)
        return maxx
        