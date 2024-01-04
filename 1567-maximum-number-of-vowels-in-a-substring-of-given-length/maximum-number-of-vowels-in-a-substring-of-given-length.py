class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        v = {"a","e","i","o","u"}
        temp = s[0:k]
        count = 0
        for ele in temp :
            if ele in v :
                count += 1
        ans = count
        for i in range(k,n):
            next = s[i]
            garbage = s[i-k]
            print(next,garbage)
            if garbage in v :
                count -= 1
            if next in v :
                count += 1
            if count > ans :
                ans = count
            
            
        return ans
        