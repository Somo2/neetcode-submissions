class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        max_key=-1
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for k,v in freq.items():
            if k==v:
                if k > max_key:
                    max_key = k
        return max_key
        
