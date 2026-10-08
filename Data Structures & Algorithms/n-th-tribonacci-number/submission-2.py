class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        if n == 0:
            return t0
        elif n == 1 or n == 2:
            return t1


        while n >= 3:
            temp = t0 + t1 + t2
            t0, t1, t2 = t1, t2, temp
            n -= 1
        return t2