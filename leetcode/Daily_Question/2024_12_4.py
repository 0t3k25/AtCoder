class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        i, j = 0, 0  # iはstr1のポインタ、jはstr2のポインタ
        n, m = len(str1), len(str2)

        while i < n and j < m:
            # 現在の文字が一致するか、1回増加させて一致する場合
            if str1[i] == str2[j] or (
                chr((ord(str1[i]) - ord("a") + 1) % 26 + ord("a")) == str2[j]
            ):
                j += 1  # str2の次の文字に進む
            i += 1  # str1の次の文字に進む

        # str2の全ての文字がチェックされた場合はTrue
        return j == m
