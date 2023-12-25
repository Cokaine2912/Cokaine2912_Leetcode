class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)
        num = 0
        for i in range(n -1 , -1 , -1) :
            num += digits[n - i - 1]*10**(i)
        n = str(num + 1)
        # print(n)
        return [int(ele) for ele in n]
        

        