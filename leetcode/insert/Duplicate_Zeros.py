from typing import List


arr = [0, 1, 1, 1]


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = 0
        i = 0
        mp = dict()
        while i + zeros < n:
            zeros += arr[i] == 0
            print(zeros)
            i += 1
        print(i + zeros)
        i - 1
        while zeros > 0:
            if i + zeros < 0:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                arr[i + zeros] = arr[i]
            i -= 1


a = Solution()
a.duplicateZeros(arr)
