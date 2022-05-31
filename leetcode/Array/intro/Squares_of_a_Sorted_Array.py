# two pointer
from multiprocessing.connection import answer_challenge


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = [None] * len(nums)
        right = len(nums) - 1
        left = 0
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[right]) > abs(nums[left]):
                answer[i] = nums[right] ** 2
                right -= 1
            else:
                answer[i] = nums[left] ** 2
                left += 1
        return answer
