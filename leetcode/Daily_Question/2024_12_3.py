class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = set(spaces)
        return "".join(
            [char if i not in spaces else f" {char}" for i, char in enumerate(s)]
        )
