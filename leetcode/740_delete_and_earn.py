# Problem: https://leetcode.com/problems/delete-and-earn/
from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        
        # count occurences of all numbers
        min_num = 10000
        max_num = 0
        for n in nums:
            dic[n] += 1
            min_num = min(n, min_num)
            max_num = max(n, max_num)

        # F(i) = max(F(i-1), F(i-2) + i * num occcurences of i)
        f_i_1, f_i_2 = 0,0
        for i in range(min_num, max_num+1):
            f_i_2, f_i_1 = f_i_1, max(f_i_1, f_i_2 + dic[i] * i)
        
        return f_i_1
        
            
        
