class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq={}
        if len(nums)%2!=0:
            return False
        
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        for v in freq.values():
            if v % 2!=0:
                return False
        return True