# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         if len(set(nums)) != len(nums):
#             return any(nums.count(i) >= 2 for i in nums)
#         return False

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         if len(set(nums)) != len(nums):
#             for i in nums:
#                 if nums.count(i) >= 2:
#                     return True
#         return False

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         return any(nums.count(i) >= 2 for i in nums) if len(set(nums)) != len(nums) else False

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)