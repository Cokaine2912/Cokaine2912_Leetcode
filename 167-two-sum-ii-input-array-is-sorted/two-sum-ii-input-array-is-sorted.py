class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i = 0
        
        n = len(nums)
        j = n - 1

        while i < j :
            if nums[i] + nums[j] > target :
                j -= 1
            elif nums[i] + nums[j] < target :
                i += 1
            elif nums[i] + nums[j] == target :
                return [i + 1 , j+ 1]
        return -1



        