class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)
        left_max = -1
        temp = 0
        if N == 1:
            arr[0] = left_max
            return arr
        for i in range(N - 1, -1, -1):
            temp = arr[i]
            arr[i] = left_max
            if temp > left_max:
                left_max = temp
        return arr
