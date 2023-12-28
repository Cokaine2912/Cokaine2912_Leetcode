class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        a = [i for i in s]
        d = {"a","e","i","o","u","A","E","I","O","U"}

        while i < j :
            if a[i] in d and a[j] in d  :
                a[i],a[j] = a[j],a[i]
                i += 1
                j -= 1
            elif a[i] in d and a[j] not in d :
                j -= 1
            elif a[i] not in d and a[j] in d :
                i += 1
            else :
                i += 1
                j -= 1
        return "".join(a)



        