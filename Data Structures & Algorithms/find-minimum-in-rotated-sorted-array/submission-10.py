class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        mini=nums[-1]
        left,right=0,n-1

        while left<=right:
            mid=(left+right)//2

            if nums[mid]<nums[right]:
                mini=min(nums[mid],mini)
                right=mid-1
            else:
                mini=min(nums[mid],mini)
                left=mid+1
        return mini