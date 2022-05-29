from itertools import count
from typing import Counter


class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        N = len(A)
        counter = 1

        for i in range(N - 1, 0, -1):
            if A[i] == A[i - 1]:
                del A[i]
            else:
                counter += 1
        return counter
