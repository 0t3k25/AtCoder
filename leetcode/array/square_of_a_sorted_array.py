class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, pointer = 0, len(nums) - 1, len(nums) - 1
        ans = [None] * len(nums)

        while pointer >= 0:
            if abs(nums[left]) < abs(nums[right]):
                ans[pointer] = nums[right] ** 2
                right -= 1
            else:
                ans[pointer] = nums[left] ** 2
                left += 1
            pointer -= 1
        return ans
