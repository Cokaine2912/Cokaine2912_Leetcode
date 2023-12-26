class Solution:
    def reverse(self, x: int) -> int:
        ans = []
        num = abs(x)
        while num > 0 :
            ans.append(num % 10)
            num = (num - num%10)//10
        result = 0
        n = len(ans)
        for i in range(n-1,-1,-1) :
            result += ans[i]*10**(n-i-1)
        if result > 2**31 - 1 :
            return 0
        elif result < -1*2**31 - 1 :
            return 0
        return result if x > 0 else -1*result


        