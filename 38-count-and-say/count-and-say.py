class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1 :
            return "1"
        
        bol = self.countAndSay(n - 1)
        
        ans = ""
        ct = 1
        for i in range(len(bol)) :
            if i == len(bol) - 1 or bol[i] != bol[i + 1] :
                ans += str(ct) + bol[i]
                ct = 1
            else :
                ct += 1
        return ans  



        