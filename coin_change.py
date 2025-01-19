# Program to implement coin change problems using greedy algorithm
def coin_change(amount, coins):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

amount = 48
coins = [1, 5, 10, 25]
print(f"Coins for {amount} cents using greedy algorithm:", coin_change(amount, coins))

