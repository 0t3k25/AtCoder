class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s_n = sorted(set(nums))
        if len(s_n) >= 3:
            return s_n[-3]
        else:
            return s_n[-1]
