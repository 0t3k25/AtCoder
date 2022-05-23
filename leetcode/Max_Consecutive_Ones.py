class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if sum(nums) == 0:
            return 0
        top = 0
        counter = 0
        for num in nums:
            if num == 1:
                counter += 1
            else:
                counter = 0
            if counter > top:
                top = counter
        return top
