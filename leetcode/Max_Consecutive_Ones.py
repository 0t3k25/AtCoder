class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        counter = 0
        for num in nums:
            if num == 1:
                counter += 1
            else:
                counter = 0
            if counter > max:
                max = counter
        print(max)
