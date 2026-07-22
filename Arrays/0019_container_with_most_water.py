class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n-1
        max_area = 0

        while left<right:
            width = right-left
            ht = min(height[left],height[right])
            area = width*ht

            max_area = max(max_area, area)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return max_area