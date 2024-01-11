class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if set(str1) != set(str2) :
            return ""
        n = len(str1)
        k = len(str2)

        if n == k :
            return str1 if str1 == str2 else ""

        GCD = 1

        for j in range(min(n,k) , 0,-1) :
            if n % j == 0 and k % j == 0 :
               GCD = max(GCD,j)
        print(GCD)
        q1 =  n // GCD
        q2 =  k // GCD
        print(q1,q2)
        ans = ""
        if k < n :
            ans =  str2[:GCD]
        else :
            ans = str1[:GCD]
        if ans * q1 == str1 and ans * q2 == str2 :
            return ans
        else :
            return ""  


        