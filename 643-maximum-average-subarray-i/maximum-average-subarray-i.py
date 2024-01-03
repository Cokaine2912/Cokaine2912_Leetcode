class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        temp = sum(nums[:k])
        print(temp)
        ans = temp / k
        for i in range(k,len(nums)) :
            temp = temp - nums[i-k] + nums[i]
            # print(temp)
            if temp/k > ans :
                ans = temp/k
        return ans
       