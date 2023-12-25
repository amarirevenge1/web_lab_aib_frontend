def count_knight_moves(N, M):
    dp = [[0] * M for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(M):
            if i + 2 < N and j + 1 < M:
                dp[i + 2][j + 1] += dp[i][j]
            if i + 1 < N and j + 2 < M:
                dp[i + 1][j + 2] += dp[i][j]

    return dp[N - 1][M - 1]


with open('input.txt', 'r') as file:
    N, M = map(int, file.readline().split())


result = count_knight_moves(N, M)


with open('output.txt', 'w') as file:
    file.write(str(result))
