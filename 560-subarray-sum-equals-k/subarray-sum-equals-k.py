class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        s = 0 
        n = len(nums)
        d = {}
        rs = []
        count = 0
        for i in range(len(nums)) :
            s += nums[i]
            if s == k :
                count += 1
            if s - k in d :
                count += d[s-k]
            if s in d :
                d[s] += 1
            else :
                d[s] = 1
            
    
        return count 