class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq={}

        for i in nums:  
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1

        for k in freq:
            if freq[k]>1:
                return k