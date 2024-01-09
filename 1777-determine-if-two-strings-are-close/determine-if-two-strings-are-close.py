class Solution:
    def s(arr) :
        for i in range(len(arr)- 1 ) :
            for j in range(1,len(arr)) :
                if arr[j-1] > arr[j] :
                    arr[j-1],arr[j] = arr[j],arr[j-1]
        return arr
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2) :
            return False
        d1 = {}
        for ele in word1 :
            if ele in d1 :
                d1[ele] += 1
            else :
                d1[ele] = 1
        d2 = {}
        for ele in word2 :
            if ele in d2 :
                d2[ele] += 1
            else :
                d2[ele] = 1
        
        one = [d1[i] for i in d1]
        two = [d2[j] for j in d2]

        return True if Solution.s(one) == Solution.s(two) else False