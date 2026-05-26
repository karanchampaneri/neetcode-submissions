class Solution:
    def isValid(self, s: str) -> bool:
        

        lookup = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []
        
        for char in s:
            if char in lookup: #if close bracket
                if stack and stack[-1] == lookup[char]: # if top of non-empty stack matches openbracket
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)
        
        if not stack:
            return True
        else:
            return False

     
            

