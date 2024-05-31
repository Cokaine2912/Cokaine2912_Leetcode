class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        count = 0 
        ans = []
        hold_value = nums[0]
        hold_index = 0

        n = len(nums)
        i = 0 
        while i < n :
            pick_value = hold_value 
            pick_index = hold_index
            newp = pick_value - 1
            if nums[newp] == pick_value:
                i += 1
                hold_value = nums[i % n]
            else :
                hold_value = nums[newp]
                nums[newp] = pick_value 

        for i in range(n) :
            if nums[i] != i + 1 :
                ans.append(i+1)
        return ans
        