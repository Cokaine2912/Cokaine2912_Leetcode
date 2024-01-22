class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) == 1 :
            return nums
        l = 0 
        r = len(nums)

        mid = (l + r) // 2  

        left = nums[:mid]
        right = nums[mid:]

        self.sortColors(left)
        self.sortColors(right)

        i = 0
        j = 0 
        k = 0 
        while i < len(left) and j < len(right) :
            if left[i] < right[j] :
                nums[k] = left[i]
                i += 1
            else :
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left) :
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right) :
            nums[k] = right[j]
            j += 1
            k += 1


