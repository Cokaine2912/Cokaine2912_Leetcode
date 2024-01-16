class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        for ele in s :
            if ele in d1 :
                d1[ele] += 1
            else :
                d1[ele] = 1

        for ele in t :
            if ele in d2 :
                d2[ele] += 1
            else :
                d2[ele] = 1


        return d1 == d2
         