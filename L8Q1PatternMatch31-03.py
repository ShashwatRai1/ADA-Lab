def pattern_match(text, pattern):
    # Initialize the DP table with False values
    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
    
    # Base case: both text and pattern are empty, so they match
    dp[0][0] = True
    
    # Handle patterns that start with '*'
    for j in range(1, len(pattern) + 1):
        if pattern[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    
    # Fill in the rest of the table
    for i in range(1, len(text) + 1):
        for j in range(1, len(pattern) + 1):
            # Case 1: pattern matches current character in text
            if text[i-1] == pattern[j-1] or pattern[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            # Case 2: pattern contains a '*', can match zero or more characters
            elif pattern[j-1] == '*':
                dp[i][j] = dp[i][j-2]  # '*' matches zero characters
                if text[i-1] == pattern[j-2] or pattern[j-2] == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j]  # '*' matches one or more characters
                
    # Return the final value in the DP table
    return dp[-1][-1]

# Example usage
text = "aab"
pattern = "c*a*b"
if pattern_match(text, pattern):
    print("Pattern matched")
else:
    print("Pattern not matched")
