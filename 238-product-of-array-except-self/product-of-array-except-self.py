class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = []
        temp = 1
        for i in range(n) :
            left.append(temp)
            temp = temp*nums[i]
        

        right = []
        temp = 1
        for i in range(n-1,-1,-1):
            right.append(temp)
            temp = temp * nums[i]
        right = right[-1::-1]

        for i in range(n) :
            right[i] = right[i] * left[i]

        return right

        