class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        k1=list(set(nums1)-set(nums2))
        k2=list(set(nums2)-set(nums1))

        return [k1,k2]