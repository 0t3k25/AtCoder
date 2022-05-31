class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rsplit()[-1])
