from typing import List


nums = [1, 2, 1, 4]
val = 1


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == val:
                del nums[i]
            i -= 1
        print(nums)


a = Solution()
a.removeElement(nums, val)
