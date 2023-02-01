class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low=0
        high=len(height)-1
        area=0
        while low < high:
            least_height=min(height[low], height[high])
            if(area<least_height*(abs(high-low))):
                area=least_height*(abs(high-low))
            if height[low] < height[high]:
                low+=1
            else:
                high-=1
        return area