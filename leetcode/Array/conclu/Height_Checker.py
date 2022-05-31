class Solution:
    def heightChecker(self, A: List[int]) -> int:
        return sum(A1 != A2 for A1, A2 in zip(A, sorted(A)))
