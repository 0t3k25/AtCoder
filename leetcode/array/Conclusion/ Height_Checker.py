class Solution:
    def heightChecker(self, arr: List[int]) -> int:
        sort_arr = sorted(arr)
        counter = 0
        for i in range(len(arr)):
            if sort_arr[i] != arr[i]:
                counter += 1
        return counter
