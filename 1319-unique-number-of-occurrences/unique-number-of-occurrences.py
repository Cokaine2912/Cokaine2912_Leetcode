class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        d = {}
        for ele in arr :
            if ele in d :
                d[ele] += 1
            else :
                d[ele] = 1

        counts = set()
        for ele in d :
            if d[ele] not in counts :
                counts.add(d[ele])
            else :
                return False

        return True