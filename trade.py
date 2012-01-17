#!/usr/bin/env python3
from imports import *

class Trade(object):
    def __init__(self, date, price_int, amount_int, tid,
                 price_currency, item, trade_type, **args):
        self.date = date; self.id = int(tid)
        self.price = int(price_int)/FACTORS[price_currency]
        self.amount = int(amount_int)/FACTORS[item]
        self.type = trade_type
        self.currency = price_currency
        self.item = item

    def __gt__(self,x):
        assert(isinstance(x, Trade))
        return self.id > x.id

    def __lt__(self,x):
        assert(isinstance(x, Trade))
        return self.id < x.id

    def __eq__(self,x):
        assert(isinstance(x, Trade))
        return self.id == x.id

    def __ne__(self,x):
        assert(isinstance(x, Trade))
        return self.id != x.id

    def __ge__(self,x):
        assert(isinstance(x, Trade))
        return self.id >= x.id

    def __le__(self,x):
        assert(isinstance(x, Trade))
        return self.id <= x.id

class Trades(object):
    def __init__(self):
        self.trades = []

    def __add__(self, x):
        assert(isinstance(x, Trade))
        self.trades.append(x)
        self.trades.sort()
        return self

    def __iter__(self):
        return iter(self.trades)

    def update(self):
        req = urlopen(API_1_URL+URLS['trades'])
        data = json.loads(req.read().decode())
        for trade in data:
            self.trades.append(Trade(**trade))
        self.trades.sort()