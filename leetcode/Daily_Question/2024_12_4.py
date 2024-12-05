class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = j = 0
        m, n = len(str1), len(str2)

        while i < m and j < n:
            if (
                str1[i] == str2[j]
                or chr((ord(str1[i]) - ord("a") + 1) % 26 + ord("a")) == str2[j]
            ):
                j += 1

            i += 1

        return j == n
