class Solution:
    def moveZeroes(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(A)
        for i in range(N - 1, -1, -1):
            if A[i] == 0:
                del A[i]
                A.append(0)
