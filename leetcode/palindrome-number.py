class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        if string == string[::-1]:
            return True
        return False
