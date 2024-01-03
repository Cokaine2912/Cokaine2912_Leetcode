class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        temp = [0]
        ans = 0
        for ele in gain :
            temp.append(temp[-1] + ele)
            if temp[-1] > ans :
                ans = temp[-1]
        return ans
        