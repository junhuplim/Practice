for _ in range(int(input())):
    s = input()
    n = len(s)
    dp = [[0,0] for i in range(n)]

    if s[0] == '0':
        dp[0][0] = 1
    elif s[0] == '1':
        dp[0][1] = 1
    else:
        dp[0][0] = 1
        dp[0][1] = 1
    for i in range(1, n):
        if s[i] == '?':
            dp[i][0] = dp[i-1][1] + 1
            dp[i][1] = dp[i-1][0] + 1
        elif s[i] == '1':
            dp[i][0] = 0
            dp[i][1] = dp[i-1][0] + 1
        else:
            dp[i][0] = dp[i-1][1] + 1
            dp[i][1] = 0

    ans = 0
    for i, j in dp:
        ans += max(i, j)
    print(ans)
