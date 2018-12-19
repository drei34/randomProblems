class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = [None for _ in range(len(height))]
        right = [None for _ in range(len(height))]
        
        for i in range(len(height)):
            if i == 0:
                left[i] = height[i]
            else:
                left[i] = max(height[i], left[i-1])
                
        for i in range(len(height)-1, -1, -1):
            if i == len(height) - 1:
                right[i] = height[i]
            else:
                right[i] = max(height[i], right[i+1])
                
        water = 0
        
        for i in range(len(height)):
            water += min(left[i],right[i]) - height[i]
            
        return water
        
