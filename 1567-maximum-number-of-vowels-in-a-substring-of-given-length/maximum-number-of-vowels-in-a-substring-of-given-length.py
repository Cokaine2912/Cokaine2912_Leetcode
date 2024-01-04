class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        v = {"a","e","i","o","u"}
        count = 0
        temp = s[0:k]
        for ele in temp :
            if ele in v :
                count += 1
        ans = count
        for i in range(k,len(s)):
            next = s[i]
            garbage = s[i-k]
            if garbage in v :
                count -= 1
            if next in v :
                count += 1
            if count > ans :
                ans = count  
        return ans
        