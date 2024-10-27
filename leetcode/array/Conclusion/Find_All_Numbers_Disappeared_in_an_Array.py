class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s_n = set(nums)
        number = []
        for i in range(1, len(nums) + 1):
            if i not in s_n:
                number.append(i)
        return number
