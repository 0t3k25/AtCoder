class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([int(log10(i)) % 2 for i in nums])
