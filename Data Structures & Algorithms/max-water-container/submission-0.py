class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        largest = 0
        while l<r:
            vol = (r-l)*min(heights[l],heights[r])
            largest = max(largest,vol)
            if heights[l] > heights[r]:
                r-=1
            else: 
                l+=1
        return largest
