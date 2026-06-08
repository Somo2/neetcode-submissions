class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        s=sorted(nums)
        pair1=s[-2:]
        pair2=s[:2]

        first=pair1[0]*pair1[1]
        second=pair2[0]*pair2[1]
        return first-second