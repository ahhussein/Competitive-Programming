class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        dp[len(nums)-1] = 1
        max_length = 1
        for i in reversed(range(0, len(nums)-1)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    max_length = max(dp[i], max_length)
        
        return max_length
                
                
                
            
        
