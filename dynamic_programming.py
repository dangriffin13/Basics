


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


arr = [1,4,0,5,-3,20,-1,6,12,-10,4,1,1,1,8,10,12,9,5,1]

#max non-adjacent subset of an array
def max_subset_sum(arr):
    n = len(arr)
    back_2 = arr[0]
    back_1 = max(arr[0],arr[1])
    for i in range(2,n):
        val = arr[i]
        new_max = max(val, back_1, val + back_2)
        back_2 = back_1
        back_1 = new_max

    return back_1