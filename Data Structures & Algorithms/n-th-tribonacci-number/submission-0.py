class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        # return t0 if n == 0 else pass
        # return t1 if n == 1 else pass
        # return t2 if n == 2 else pass

        while n >= 3:
            temp = t0 + t1 + t2
            t0, t1, t2 = t1, t2, temp
            n -= 1
        return t2