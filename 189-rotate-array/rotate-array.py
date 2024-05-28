class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        count = 0 
        cycle = 0 
        n = len(nums)
        if k % n == 0 :
            return nums
        hold_value = nums[0]
        hold_index = 0
        while count < n :
            pick_value = hold_value
            pick_index = hold_index
            newp = (pick_index + k) % n 
            hold_value = nums[newp]
            nums[newp] = pick_value
            hold_index = newp
            if hold_index == cycle :
                cycle += 1
                hold_index = cycle
                hold_value = nums[cycle]
            count += 1
        return nums 

            
        