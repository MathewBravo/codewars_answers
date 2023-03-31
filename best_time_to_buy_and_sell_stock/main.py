from typing import List


def maxProfit(prices: List[int]) -> int:
    min_val = float('inf')
    profit = 0
    for i, vali in enumerate(prices):
        if i < min_val:
            min_val = i
        elif i - min_val > profit:
            profit = i - min_val

    return profit




if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices=prices))
