class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hello = []
        while strs:
            hello.append([strs.pop(0)])
            for j in strs[:]:
                if len(hello[-1][0]) == len(j) and sorted(hello[-1][0]) == sorted(j):
                    hello[-1].append(j)
                    strs.remove(j)
        return hello