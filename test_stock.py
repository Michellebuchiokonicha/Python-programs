from stock import max_profit, max_profit2

def test_stock():
    for fn in (max_profit, max_profit2):
        assert fn([7, 1, 5, 3, 6, 4]) == 5, "buy at 1, day 1, sell at 6, day 4"
        assert  fn([7, 6, 4, 3, 1]) == 0, "prices only fall, so never buy"
        assert  fn([2,4,1]) == 2, "buy 2, sell 4; the later 1 is too late to help"
        assert  fn([1]) == 0, "only one day, so you can't sell"
        assert  fn([3,3,3]) == 0, "flat prices, no profit"
        assert  fn([2,1,2,1,0, 1,2]) == 2, "buy at 0, sell at 2"


FUNCTIONS = (max_profit, max_profit2)

def test_example_buy_low_sell_high():
    for fn in FUNCTIONS:
        assert fn([7, 1, 5, 3,6, 4]) == 5, f"{fn.__name__}: buy at 1, sell at 6"


def test_best_trade_not_global_min_or_max():
    for fn in FUNCTIONS:
        assert fn([3,10, 1, 2]) == 7, f"{fn.__name__}: buy 3, sell 10; the later 1 is too late"
