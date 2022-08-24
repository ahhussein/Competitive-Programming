# problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_array_ptr = 0
        for i in range(len(nums)):
            if i == 0:
                continue
            
            if nums[i] != nums[i-1]:
                unique_array_ptr += 1
                nums[unique_array_ptr] = nums[i]
        
        return unique_array_ptr+1

