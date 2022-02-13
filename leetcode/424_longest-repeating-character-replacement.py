class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_left = 0
        window_right = 0
        max_length = 0
        count_dict = collections.Counter()
        max_frequency = 0
        while window_right < len(s):
            count_dict[s[window_right]] += 1
            
            current_length = window_right - window_left + 1 
            
            max_frequency = max(max_frequency, count_dict[s[window_right]])
                
            if current_length - max_frequency <= k:
                max_length = max(max_length, current_length)
            else:
                count_dict[s[window_left]] -= 1
                window_left += 1
            window_right += 1
        return max_length
            
