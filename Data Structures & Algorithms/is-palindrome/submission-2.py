class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        def isValid(c):

            if (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9')):
                return True
            else:
                return False

        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not isValid(s[left]):
                left +=1

            while right > left and not isValid(s[right]):
                right -=1

            if s[left].lower() != s[right].lower():
                return False

            left +=1
            right -=1

        return True
            

