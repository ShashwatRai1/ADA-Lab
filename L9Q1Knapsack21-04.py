def knapsack_dp(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtracking to get selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    
    return dp[n][capacity], selected_items[::-1]


# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
max_value, selected_items = knapsack_dp(weights, values, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)