class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[(abs(nums[i]) - 1)] > 0:
                nums[(abs(nums[i]) - 1)] = -nums[(abs(nums[i]) - 1)]
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res
        # s_n = set(nums)
        # number = []
        # for i in range(1, len(nums) + 1):
        #     if i not in s_n:
        #         number.append(i)
        # return number
