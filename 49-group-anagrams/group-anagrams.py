class Solution:
    def groupAnagrams(self, strs) :
        

        d = {}

        for ele in strs :
            # print(d)
            s = "".join(sorted(ele))
            if s in d :
                temp = d[s]
                temp.append(ele)
                d[s] = temp
            else :
                d[s] = [ele]

        # print(d)
        
        ans = []
        for ele in d :
          ans.append(d[ele])
        return ans
        