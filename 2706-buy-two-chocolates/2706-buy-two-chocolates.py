class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_price = min(prices)
        prices.remove(min_price)
        second_min_price = min(prices)
        
        left_over = money - min_price - second_min_price
        if left_over < 0:
            return money
        return left_over