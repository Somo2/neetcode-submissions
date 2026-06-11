class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums2=sorted(nums)
        return nums2[0]