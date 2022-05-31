class Solution:
    def removeElement(self, A: List[int], val: int) -> int:
        i = 0
        N = len(A)
        for j in range(0, N):
            if val[j] != val:
                val[i] = val[j]
                i += 1
            return i
