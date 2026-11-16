class Solution:
    def climbStairs(self, n: int) -> int:
        cache = []
        if n==1: return 1
        cache.append(1)
        cache.append(2)
        for _ in range(3, n+1):
            cache.append(cache[-1]+cache[-2])
        return cache[-1]

        