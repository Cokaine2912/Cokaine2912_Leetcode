class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums) - 1
        left = [nums[0]]
        right = [nums[n]]

        for i in range(1,n + 1):
            left.append(left[-1] + nums[i])
        for j in range(n - 1,-1,-1) :
            right.append(right[-1] + nums[j])
        right = right[-1::-1]
        # print(left,right)

        for k in range(n + 1) :
            if right[k] == left[k] :
                return k
        
        
        return -1
        