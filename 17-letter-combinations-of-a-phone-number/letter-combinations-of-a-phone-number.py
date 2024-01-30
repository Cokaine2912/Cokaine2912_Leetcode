class Solution:
    d = {
        2 : "abc",
        3 : "def",
        4 : "ghi",
        5 : "jkl",
        6 : "mno",
        7 : "pqrs",
        8 : "tuv",
        9 : "wxyz"
        }
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits :
            return []
        elif len(digits) == 1 :
            return [k for k in Solution.d[int(digits)]]
        temp = []

        for ele1 in Solution.d[int(digits[0])] :
            for ele2 in self.letterCombinations(digits[1 : ]) :
                temp.append(ele1 + ele2)

        return temp                 
