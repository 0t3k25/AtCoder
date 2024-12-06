class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_", "") != target.replace("_", ""):
            return False

        n = len(start)
        s_idx = t_idx = 0
        while s_idx < n and t_idx < n:
            while s_idx < n and start[s_idx] == "_":
                s_idx += 1
            while t_idx < n and target[t_idx] == "_":
                t_idx += 1

                # 両方のインデックスが範囲外なら終了
            if s_idx == n and t_idx == n:
                break

            if (s_idx == n) != (t_idx == n):
                return False

            if start[s_idx] == "L" and s_idx < t_idx:
                return False
            if start[s_idx] == "R" and s_idx > t_idx:
                return False
            s_idx += 1
            t_idx += 1

        return True
