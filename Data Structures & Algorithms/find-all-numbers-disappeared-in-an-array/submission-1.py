class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m=len(nums)
        new=set(list(range(1,m+1)))
        res=[]
        for i in new:
            if i not in nums:
                res.append(i)
        return res