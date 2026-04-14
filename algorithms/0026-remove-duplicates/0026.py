class Solution:
    def removeDuplicates(self, nums: list) -> int:
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                del nums[i]

        return len(nums)