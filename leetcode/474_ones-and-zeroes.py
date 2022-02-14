class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp =  [[0 for x in range(m+1)] for y in range(n+1)]
        for str_i in strs:
            num_ones = str_i.count('1')
            num_zeros = str_i.count('0')
            for ones_idx in reversed(range(num_ones, n+1)):
                for zeros_idx in reversed(range(num_zeros, m+1)):
                    # Current max, or max of admitting `str_i` if fits
                    dp[ones_idx][zeros_idx] = max(dp[ones_idx][zeros_idx], dp[ones_idx - num_ones][zeros_idx - num_zeros]+1)
        return dp[n][m]
                    
