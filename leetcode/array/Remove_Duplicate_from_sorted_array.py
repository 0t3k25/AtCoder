class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1, counter = 0, 1
        for num in nums:
            if num != nums[p1]:
                p1 += 1
                counter += 1
                nums[p1] = num
        return counter
