class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if d.get(i,0) == 1:
                return True
            d[i] =1
        return False