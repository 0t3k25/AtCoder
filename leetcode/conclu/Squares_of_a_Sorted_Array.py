class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        right = 0
        i = len(nums) - 1
        left = len(nums) - 1
        while True:
            if right > left:
                return res
            if abs(nums[right]) > abs(nums[left]):
                res[i] = nums[right] ** 2
                right += 1
                i -= 1
            elif abs(nums[right]) < abs(nums[left]):
                res[i] = nums[left] ** 2
                left -= 1
                i -= 1
            elif abs(nums[right]) == abs(nums[left]):
                res[i] = nums[right] ** 2
                right += 1
                i -= 1
