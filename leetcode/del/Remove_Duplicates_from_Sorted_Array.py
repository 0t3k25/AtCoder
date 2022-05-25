class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return len(nums)
        j = 0
        for i in nums:
            if i != nums[j]:
                j += 1
                nums[j] = i
        return j + 1
