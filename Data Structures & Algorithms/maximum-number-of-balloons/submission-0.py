class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq={}
        for i in text:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        b = freq.get('b', 0)
        a = freq.get('a', 0)
        l = freq.get('l', 0)
        o = freq.get('o', 0)
        n = freq.get('n', 0)
        result = min(b, a, l//2, o//2, n)
        return result