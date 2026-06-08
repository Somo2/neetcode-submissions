class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr=s.strip()
        c=arr.split(" ")
        return len(c[-1])