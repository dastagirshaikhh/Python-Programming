def lcs(s1, s2):
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = ""
    i = len(s1)
    j = len(s2)

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs += s1[i - 1]
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return lcs[::-1]


if __name__ == "__main__":
    print(lcs("aidfhr", "abedgh"))
