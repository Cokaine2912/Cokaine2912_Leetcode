class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        one = 2**31 - 1

        two = 2**31 - 1

        for third in nums :
            if third < one :
                one = third
            elif third < two and third > one :
                two = third
            elif third > two :
                return True
        return False     
        