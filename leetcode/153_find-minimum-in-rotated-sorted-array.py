class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.binarySearch(0, len(nums)-1, nums)
        
    def binarySearch(self, index_from, index_to, nums):
        if index_from > index_to:
            return nums[0]
        
        mid = (index_from + index_to)//2
        
        
        if nums[mid] < nums[0]:
            index_to = mid - 1
        else:
            index_from = mid + 1
                
        if mid + 1 < len(nums) and nums[mid+1] < nums[mid]:
            return nums[mid+1]
        if mid - 1 > 0 and nums[mid-1] > nums[mid]:
            return nums[mid]

            
        return self.binarySearch(index_from, index_to, nums)
        
        
