class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}

        # count magazine letters
        for ch in magazine:
            freq[ch] = freq.get(ch, 0) + 1

        # try to build ransomNote
        for ch in ransomNote:
            if ch not in freq or freq[ch] == 0:
                return False
            freq[ch] -= 1

        return True