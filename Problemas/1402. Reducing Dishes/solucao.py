from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        
        total = 0
        atual = 0
        
        for s in satisfaction:
            atual += s
            if atual > 0:
                total += atual
            else:
                break
        
        return total
