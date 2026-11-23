# list prices of stock
# so the prices are listed, the index are the days.
# since you can't buy and sell on a previous day only later days so index can not badd -1
#  it can loop through the remaining but not what is behind
# s†art from index 0, check for the lowest price so far, if no price less than it previously, oprofit will be zero, best so far 0
# you move to the next index and do samething, check for the lwest price before it, if none, return 0. if there is, remove that from it, then check if any previous substitution is greater than it
def max_profit(prices: list[int]) -> int:
    lowest_so_far = prices[0]
    best_so_far = 0
    profit = 0
    for day in range(len(prices)):
       
        if prices[day] < lowest_so_far:
            lowest_so_far = prices[day]
            
        if lowest_so_far < prices[day]:
            profit = prices[day] - lowest_so_far
        if lowest_so_far > prices[day]:
            profit = 0
        if best_so_far < profit:
            best_so_far = profit
    return best_so_far


def max_profit2(prices: list[int]) -> int:
    lowest_so_far = float("inf")
    best_so_far = 0
    for price in prices: 
        if price < lowest_so_far:
            lowest_so_far = price
        profit = price - lowest_so_far
        if profit > best_so_far:
            best_so_far = profit
    return best_so_far

    