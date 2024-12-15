class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[left] < nums[mid]:
                right = mid - 1
            else:
                left = mid

        return left
