class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0  # p1 zero-pointer
        for i in range(len(nums)):
            if nums[i] != val:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1
        return p1
