class Solution:

    def days(arr,payload) :
        day = 1
        load = 0 

        for ele in arr :
            if load + ele <= payload :
                load += ele
            else :
                day += 1
                load = ele
        return day

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        low = max(weights)
        high = sum(weights)

        while low <= high :
            mid = (low + high) // 2 

            if Solution.days(weights,mid) > days :
                low = mid + 1
            else :
                high = mid - 1
        
        return low


        