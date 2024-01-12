class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        one = 2**31 - 1

        two = 2**31 - 1

        for third in nums :
            if third <= one :
                one = third
            elif third <= two :
                two = third
            if one < two < third :
                return True 
        return False     
        