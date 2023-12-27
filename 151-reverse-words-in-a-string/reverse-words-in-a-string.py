class Solution:
    def reverseWords(self, s: str) -> str:

        temp = s.split(" ")
        
        ans = ""
        for ele in temp[-1::-1] :
            if ele != "" :
                ans += ele + " "
        return ans[:-1]



        