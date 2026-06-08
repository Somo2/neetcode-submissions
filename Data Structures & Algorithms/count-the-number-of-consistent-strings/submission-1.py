class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = [word for word in words if set(word) <= set(allowed)]
        return len(s)