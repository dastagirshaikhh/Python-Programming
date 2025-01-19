def NaiveSearch(pattern, text):
    m = len(pattern)
    n = len(text)

    for i in range(n - m + 1):
        j = 0
        while j < m:
            if text[i + j] != pattern[j]:
                break

            j += 1
        if j == m:
            print("Text found at index %s" % i)
            # return i
        # if j != m:
            # print("pattern not found")


s = "this is a test"
p = "taste"
NaiveSearch(p, s)
