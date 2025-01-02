class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ret = [-1, -1]
        if not nums:
            return ret

        # find left index
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if target == nums[left]:
            ret[0] = left
        else:
            return ret

        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2 + 1
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        ret[1] = right

        return ret
