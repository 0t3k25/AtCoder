class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]  # 要素が1つの場合はそのまま早期リターン

        right_val = arr[-1]  # 最後の要素を保存し、最初に -1 に置き換える
        arr[-1] = -1

        # 右から左に向かって最大の要素を更新
        for i in range(len(arr) - 2, -1, -1):
            arr[i], right_val = right_val, max(right_val, arr[i])

        return arr
