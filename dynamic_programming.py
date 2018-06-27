


coins = [1, 2, 5]

combos = [1] + [0] * 11

for coin in coins:
    print('coin ', coin)
    for i in range(coin, 12):
        print('coin:' , coin, '  i:', i, '  i-coin:', i-coin)
        combos[i] += combos[i-coin]
        print('combos ', combos)

def all_coin_change_combinations(amount_to_divide, coin_array):
    combos = [1] + [0] * amount_to_divide
    for coin in coin_array
        for i in range(coin, amount_to_divide+1):
            combos[i] += combos[i-coin]
    return combos[amount_to_divide]