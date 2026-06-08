class Solution:
    def maxDifference(self, s: str) -> int:
        freq={}
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        odd = []
        even = []

        for v in freq.values():
            if v % 2 == 1:
                odd.append(v)
            else:
                even.append(v)

        return max(odd) - min(even)