class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        y=len(piles)
        n,su=y-2,0
        while n>=y//3:
            su+=piles[n]
            n-=2
        return su
