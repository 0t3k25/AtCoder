class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, count = 0, 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                ans = max(count, ans)
                count = 0
        return max(count, ans)
