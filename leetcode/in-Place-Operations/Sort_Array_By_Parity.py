class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        N = len(A)
        left = 0
        right = N - 1
        while N > 1:
            if A[left] % 2 == 0:
                left += 1
                if left > right or left == right:
                    return A
                continue
            if A[right] % 2 == 1:
                right -= 1
                if left > right or left == right:
                    return A
                continue
            A[left], A[right] = A[right], A[left]
        return A
