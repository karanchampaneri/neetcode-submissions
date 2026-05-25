class Solution:
    def isPalindrome(self, s: str) -> bool:
        # phrase = s.replace(" ","").strip().lower()

        # print(phrase)

        # for i in range(len(phrase)):
        #     if phrase[i] != phrase[-i]:
        #         return False

        phrase = ''
        for char in s:
            if char.isalnum():
                phrase += char.lower()

        left = 0
        right = len(phrase) - 1

        while left < right:
            if phrase[left] != phrase[right]:
                return False
            left +=1 
            right -= 1

        return True