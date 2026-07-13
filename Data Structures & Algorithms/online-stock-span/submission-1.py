class StockSpanner:

    def __init__(self):
        self.stack = [] # Storing the data structure of (price, res)

    def next(self, price: int) -> int:
        res = 1
        while self.stack and price >= self.stack[-1][0]:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)