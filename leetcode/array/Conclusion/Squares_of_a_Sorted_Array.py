class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lp, rp, p1 = 0, len(nums) - 1, len(nums) - 1
        ans = [None] * len(nums)

        while p1 >= 0:
            if abs(nums[lp]) > abs(nums[rp]):
                ans[p1] = nums[lp] ** 2
                lp += 1
            else:
                ans[p1] = nums[rp] ** 2
                rp -= 1
            p1 -= 1

        return ans
