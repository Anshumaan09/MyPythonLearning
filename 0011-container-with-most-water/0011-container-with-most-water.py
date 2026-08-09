class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_storage = 0
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            curr_storage = w * h
            max_storage = max(curr_storage, max_storage)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        
        return max_storage