class Solution:
    def asteroidCollision(self, aster: List[int]) -> List[int]:

        stack = []

        i = 0 
        n = len(aster)
        while i < n :
            stack.append(aster[i])
            while stack and len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0 :
                if stack[-1] + stack[-2] < 0 :
                    val = stack[-1]
                    stack.pop()
                    stack[-1] = val
                elif stack[-1] + stack[-2] == 0 :
                    stack.pop()
                    stack.pop()
                elif stack[-1] + stack[-2] > 0 :
                    val = stack[-2]
                    stack.pop()
                    stack[-1] = val
            i += 1
        return stack

        