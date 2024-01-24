class Solution:
    def simplifyPath(self, path: str) -> str:

        k = path.split("/")
        print(k)
        
        stack = []
        for ele in k :
            if ele == "" or ele == "/" or ele =="." :
                pass
            elif stack and ele == ".." :
                stack.pop()
            elif not stack and ele == ".." :
                pass
            else :
                stack.append(ele)
        print(stack)
        ans = ""
        for ele in stack :
            ans += "/" + ele

        return ans if stack else "/"

            
        