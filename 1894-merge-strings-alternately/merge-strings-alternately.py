class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        w1 = len(word1)
        w2 = len(word2)
        ans = ""
        i = 0
        j = 0
        while i < w1 and j < w2 :
            ans += word1[i]
            i += 1
            ans += word2[j]
            j += 1
        
        if i < w1 :
            ans += word1[i:]
        elif j < w2 :
            ans += word2[j:]

        return ans
        