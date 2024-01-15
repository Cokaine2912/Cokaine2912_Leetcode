class Solution:
    def groupAnagrams(self, strs) :
        
        d = {}

        for ele in strs :
            
            s = "".join(sorted(ele))
            if s in d :
                temp = d[s]
                temp.append(ele)
                d[s] = temp
            else :
                d[s] = [ele]

      
        
        ans = [d[k] for k in d]
        
        return ans
        