class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_volume = 0
        i,j = 0,n-1

        while i<j:
            if heights[i]<heights[j]:
                vol = heights[i]*(j-i)
                i+=1
            elif heights[i]>heights[j]:
                vol = heights[j]*(j-i)
                j-=1
            else:
                vol = heights[i]*(j-i)
                i+=1
                j-=1

            max_volume =  max(max_volume,vol)

        return max_volume