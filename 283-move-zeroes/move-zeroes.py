class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0


        for j in range(len(nums)) :
            if nums[j] != 0 and nums[i] == 0 :
                nums[i],nums[j] = nums[j],nums[i]
            if nums[i] != 0 :
                i += 1


        # while j < len(nums) and i < len(nums) - 1  :
        #     # print("Start",i,j)
        #     while j < len(nums) - 1 and nums[j] == 0 :
        #         j += 1
        #     while i < len(nums) - 1 and nums[i] != 0 :
        #         i += 1
        #     # print("Sec",i,j)
        #     if i != j :
        #         nums[i] , nums[j] = nums[j] , nums[i]
        
        #         i += 1
        #     # print(i,j)
