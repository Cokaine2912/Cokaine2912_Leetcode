class Solution:
    def check(self, nums: List[int]) -> bool:
        last = -1 * 2**31
        i = 0
        while i < len(nums) and nums[i] >= last :
            last = nums[i]
            i += 1

        if i >= len(nums) :
            return True

        nums = list(nums[i : ]) + list(nums[:i])
        print(nums , i)
        last = -1 * 2**31

        for ele in nums:
            if ele < last :
                return False 
            last = ele
        return True


