class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = collections.Counter(nums)
        res = []
        for i in range(1, len(nums) + 1):
            if i not in N:
                res.append(i)
        return res
