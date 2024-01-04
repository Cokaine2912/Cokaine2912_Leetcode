class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d1 = {}
        d2 = {}

        for ele in nums1:
            if ele in d1 :
                d1[ele] += 1
            else :
                d1[ele] = 1

        for ele in nums2:
            if ele in d2 :
                d2[ele] += 1
            else :
                d2[ele] = 1
        
        

        ans1 = []
        ans2 = []
        for ele in d1 :
            if ele in d2 :
                pass
            else :
                ans1.append(ele)

        for ele in d2 :
            if ele in d1 :
                pass
            else :
                ans2.append(ele)

        
        return [ans1,ans2]
        