from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = defaultdict(list)
        for employee_idx, manager_idx in enumerate(manager):
            if manager_idx == -1:
                continue
            subordinates[manager_idx].append(employee_idx)
        return self.timeToInform(headID, subordinates, informTime)
        
    
    def timeToInform(self, headID, subordinates, informTimes):
        if not subordinates[headID]:
            return 0
        
        maxTimeSubordinates = 0
        for subordinate in subordinates[headID]:
            timeSubordinate = self.timeToInform(subordinate, subordinates, informTimes)
            if timeSubordinate > maxTimeSubordinates:
                maxTimeSubordinates = timeSubordinate
            
        return informTimes[headID] + maxTimeSubordinates
            
       
