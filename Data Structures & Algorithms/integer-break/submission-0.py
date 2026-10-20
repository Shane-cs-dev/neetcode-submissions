class Solution:
    def integerBreak(self, n: int) -> int:
        res = 0
        for i in range(1, n):
            if n % i == 0:
                count = n // i
                res = max(res, i ** count)
        return res
            