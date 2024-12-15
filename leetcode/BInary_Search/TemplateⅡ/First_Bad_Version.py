# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        result = 1

        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1
                result = mid
        return result
