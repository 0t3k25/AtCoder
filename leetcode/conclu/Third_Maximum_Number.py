class Solution:
    def thirdMax(self, A: List[int]) -> int:
        A_list = list(set(A))
        A_sorted = sorted(A_list, reverse=True)
        if len(A_sorted) > 2:
            return A_sorted[2]
        return A_sorted[0]
