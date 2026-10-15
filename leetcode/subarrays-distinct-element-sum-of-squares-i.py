class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        summa = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                s = set()
                x = [s.add(d) for d in nums[i:j]]
                summa += len(s)**2
        return summa