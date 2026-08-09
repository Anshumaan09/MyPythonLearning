class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windows_sum  = sum(nums[:k])
        max_sum = windows_sum

        for i in range(k,len(nums)):
            windows_sum += nums[i]
            windows_sum -= nums[i-k]
            max_sum = max(max_sum, windows_sum)
        
        avg = max_sum/k
        return avg
