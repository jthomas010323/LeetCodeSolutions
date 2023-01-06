class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        bars=0
        costs.sort()
        for i in range(len(costs)):
            if costs[i]<=coins:
                bars+=1
                coins-=costs[i]
            elif costs[i]>coins:
                break
        return bars
                
        