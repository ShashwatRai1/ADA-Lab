def find_kicks(N, A, B):
    # Initialize the dp table with 0s
    dp = [[0]*(A+1) for _ in range(N+1)]

    # Fill the dp table using the recurrence relation
    for i in range(1, N+1):
        for j in range(1, A+1):
            if j < B[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-B[i-1]] + 1)

    # Find the lexicographically smallest order of friends to kick Tushar
    kicks = []
    i, j = N, A
    while i > 0 and j > 0:
        if dp[i][j] > dp[i-1][j]:
            kicks.append(i-1)  # Add the index of the ith friend to the list of kicks
            j -= B[i-1]  # Reduce the capacity by the strength of the ith friend
        i -= 1

    return kicks[::-1]  # Reverse the list and return

# Test the function with an example
# DRiver COde: 
if __name__ == '__main__':
    # N=2
    # A=12
    # B=[3,4]

    N = 5
    A = 11
    B = [6, 8,5,4,7]
    kicks = find_kicks(N, A, B)
    print(kicks)