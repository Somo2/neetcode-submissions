class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total=0

        for word in words:
            freq={}

            for ch in chars:
                if ch in freq:
                    freq[ch]+=1
                else:
                    freq[ch]=1

            valid=True

            for ch in word:
                if ch not in freq or freq[ch]==0:
                    valid=False
                    break
                freq[ch]-=1
            if valid:
                total += len(word)

        return total

            
