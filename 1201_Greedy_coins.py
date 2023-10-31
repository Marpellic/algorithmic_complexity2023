import math


def coinsGreedy(denominations, amount):
    amounts = [0] * len(denominations)
    for index, coin in enumerate(denominations):
        amounts[index] = math.floor(amount / coin)
        amount = amount % coin
    return amounts


denominations = [50, 25, 20, 10, 5, 1]
amount = 40

if __name__ == '__main__':
    amounts = coinsGreedy(denominations, amount)
    for i in range(len(denominations)):
        if amounts[i]: print(amounts[i], " monedas de ", denominations[i])