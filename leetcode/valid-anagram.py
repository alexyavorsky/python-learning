# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) == len(t):
#             t1 = [symbol for symbol in t]
#             for i in s:
#                 if i in t1:
#                     t1.remove(i)
#             if len(t1) == 0:
#                 return True
#         return False

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s1 = set([(symbol, t.count(symbol)) for symbol in s])
#         t1 = set([(symbol, s.count(symbol)) for symbol in t])
#         if s1 == t1:
#             return True
#         return False

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s = [i for i in s]
#         t = [i for i in t]
#         return sorted(s) == sorted(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)