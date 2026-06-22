class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        l=0
        r=n-1

        while l<r:
            area=min(heights[r],heights[l])*(r-l)
            max_area=max(area,max_area)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_area


        