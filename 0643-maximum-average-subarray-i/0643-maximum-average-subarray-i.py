class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        w_sum = sum(nums[:k])
        max_sum = w_sum
        
        for i in range(k, len(nums)):
            w_sum = w_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, w_sum)
        
        return max_sum / k