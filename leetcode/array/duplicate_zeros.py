class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        i, j = len(arr) - 1, len(arr) + zeros - 1  # define two pointer

        while i < j:
            if j < len(arr):
                arr[j] = arr[i]  # Assign value first

            if arr[i] == 0:
                j -= 1
                if j < len(arr):
                    arr[j] = arr[i]
            i -= 1
            j -= 1
