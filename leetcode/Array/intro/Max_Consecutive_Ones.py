class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = count = 0
        for num in nums:
            count += 1 if num == 1 else count == 0
            ans = max(ans, count)
        return ans
