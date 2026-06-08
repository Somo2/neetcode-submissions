class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_list = [ord(ch) for ch in s]
        total=0
        for i in range(len(ascii_list) - 1):
            total += abs(ascii_list[i + 1] - ascii_list[i])

        return total