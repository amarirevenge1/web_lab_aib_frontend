def count_routes(N, M):
    dp = [[0] * M for _ in range(N)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(M):
            if i - 2 >= 0:
                dp[i][j] += dp[i - 2][j]
            if j - 2 >= 0:
                dp[i][j] += dp[i][j - 2]
            if i - 1 >= 0 and j - 1 >= 0:
                dp[i][j] += dp[i - 1][j - 1]
    return dp[N - 1][M - 1]

N, M = map(int, input().split())
result = count_routes(N, M)
print(result)