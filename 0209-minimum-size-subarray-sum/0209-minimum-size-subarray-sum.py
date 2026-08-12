import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        min_length = math.inf

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                window_size = right - left + 1
                min_length = min(min_length, window_size)
                window_sum -= nums[left]
                left += 1
            
        if min_length == float("inf"):
            return 0

        return min_length