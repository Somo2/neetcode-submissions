class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        for l in range(n):
            for r in range(l+1, n):
                area = (r - l) * min(heights[l], heights[r])
                max_area = max(max_area, area)
        return max_area