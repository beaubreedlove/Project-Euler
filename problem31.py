
import copy

coins = [1, 2, 5, 10, 20, 50, 100, 200]

class Wallet:
    def __init__(self, coins):
        self.coins = coins
    def add_coin(self, coin):
        self.coins[coin] = self.coins.get(coin, 0) + 1
    def copy(self):
        return Wallet(copy.copy(self.coins))
    def uid(self):
        return str(self.coins)

empty_wallet = Wallet({})
one_wallet = Wallet({1:1})

cache = {
    0: {empty_wallet.uid() : empty_wallet},
    1: {one_wallet.uid() : one_wallet}
}

def combinations(n):
    ret = cache.get(n)
    if ret is not None:
        return ret

    ret = {}

    for coin in coins:
        if coin <= n:
            sub = combinations(n - coin)
            for i in sub:
                s = sub[i].copy()
                s.add_coin(coin)
                uid = s.uid()
                ret[uid] = s
        else:
            break

    cache[n] = ret

    return ret


for i in range(200):
    print "c(" + str(i+1) + ") = " + str(len(combinations(i+1))) + " [" + str(len(combinations(i+1)) - len(combinations(i))) + "]"

