class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels=list(jewels)
        stones=list(stones)
        c=0
        for jewel in jewels:
            c+=stones.count(jewel)
        return c