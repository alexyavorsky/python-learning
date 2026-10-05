class Solution:
    def maxDepth(self, s: str) -> int:
        c_left = 0
        maximum = -1
        for symbol in s:
            if symbol == "(":
                c_left += 1
            elif symbol == ")":
                c_left -= 1
            maximum = max(maximum, c_left)
        return maximum
