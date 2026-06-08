class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq={}
        count=0
        result=""
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for key,value in freq.items():
            if value==1:
                count+=1
                if count==k:
                    result=key
                    return result
        return ""
        