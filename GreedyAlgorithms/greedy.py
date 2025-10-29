"""
Greedy algorithm is an problem solving approach that works by selecting local optimums at every step, with the hope that these local optimums build to the global optimum.

Characteristics :

1. Greedy choice property : Global optimum build from the local optimums at each step

2. Optimal Substructure : Optimum solution to the problem build from the optimal solutions to the sub problems.

Greedy algorithms doesn't gurantee the optimal solution every time.

Dynamic programming is used whem we have overlapping subproblems and optimal substructure.

Greedy algorithm is used when the problem has greedy choice property and optimal substructure.


If you need fast and approximate solution use greedy.

if you need optimal and accurate use dp.

"""

coins = [1, 5, 10, 25]

def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)

    result = []

    for coin in coins: 
        while amount >= coin: # making best choices at every step.
            amount-=coin
            result.append(coin)

    return result

# this greedy algorithm doesn't give the best optimal solution for [1,3,4] for amount 6, it will return [4,1,1] but dp gives [3,3]

# print(greedy_coin_change(coins,30))


def dp_coin_change(coins, amount):

    dp = [float('inf')] * (amount+1)

    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin] + 1)

            print(dp)   

    return dp[amount] if dp[amount]!=float('inf') else -1


print(dp_coin_change([1,3,4],6))

