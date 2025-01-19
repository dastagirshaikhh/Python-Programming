# # Practical 7.1
# # Naive pattern searching
# def search(pat,txt):
#     M = len(pat)
#     N = len(txt)
#     for i in range(N-M+1):
#         j = 0

#         while(j < M):
#             if (txt[i+j] != pat[j]):
#                 break
#             j += 1
#         if (j == M):
#             print("Pattern found at index",i)

# if __name__ == '__main__':
#     txt = "hello how are you everyone are you hi how are you"
#     print("text data:-",txt)
#     pat = "are you"
#     print("find pattern :-",pat)
#     search(pat, txt)


# # Practical 7.2
# # python implementation of Rabin Karp Algorithm
# d = 256
# def search(pat, txt, q):
# 	M = len(pat)
# 	N = len(txt)
# 	i = 0
# 	j = 0
# 	p = 0
# 	t = 0
# 	h = 1
# 	for i in range(M-1):
# 		h = (h*d) % q
# 	for i in range(M):
# 		p = (d*p + ord(pat[i])) % q
# 		t = (d*t + ord(txt[i])) % q
# 	for i in range(N-M+1):
# 		if p == t:
# 			for j in range(M):
# 				if txt[i+j] != pat[j]:
# 					break
# 				else:
# 					j += 1
# 			if j == M:
# 				print("Pattern found at index " + str(i))
# 		if i < N-M:
# 			t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q
# 			if t < 0:
# 				t = t+q
# if __name__ == '__main__':
# 	txt = "GEEKS fybsc cs FOR GEEKS"
# 	pat = "GEEK"
# 	q = 101
# 	search(pat, txt, q)


# Practical 7.3
# Knuth-Morris-Pratt(KMP) Algorithm


# import string
# def KMPSearch(pat, txt):
#     M = len(pat)
#     N = len(txt)
#     lps = [0] * M
#     global j
#     j = 0
#     computeLPSArray(pat, M, lps)
#     i = 0
#     while i < N:
#         if pat[j] == txt[i]:
#             i += 1
#             j += 1
#         if j == M:
#             global index_of_optr
#             index_of_optr = i - j
#             j = lps[j - 1]
#             return index_of_optr
#         elif i < N and pat[j] != txt[i]:
#             if j != 0:
#                 j = lps[j - 1]
#             else:
#                 i += 1


# def computeLPSArray(pat, M, lps):
#     len = 0
#     lps[0]
#     i = 1
#     while i < M:
#         if pat[i] == pat[len]:
#             len += 1
#             lps[i] = len
#             i += 1
#         else:
#             if len != 0:
#                 len = lps[len - 1]
#             else:
#                 lps[i] = 0
#                 i += 1


# txt = #string from js goes here
# optrs = ["+", "-", "*", "/", "%"]
# for optr in optrs:
#     if KMPSearch(optr, txt):
#         pat = [optr]
#         pat = pat[0]


# def isInt(num):
#     if num.isdigit():
#         num = int(num)
#         return num


# print(pat)
# KMPSearch(pat, txt)


# print(index_of_optr)
# num1 = txt[:index_of_optr]
# num1 = isInt(num1)
# print(type(num1))

# num2 = txt[index_of_optr + 1 :]
# num2 = isInt(num2)
# print(type(num2))
# print(num1)
# print(num2)


# def calculate():
#     if pat == "+":
#         num3 = num1 + num2
#         return num3
#     if pat == "-":
#         num3 = num1 - num2
#         return num3
#     if pat == "*":
#         num3 = num1 * num2
#         return num3
#     if pat == "/":
#         num3 = num1 / num2
#         return num3
#     if pat == "%":
#         num3 = num1 % num2
#         return num3


# Ans = calculate()
# #result string is stored in ans variable return the ans variable to js


def Result_func(input_text):
    def KMPSearch(pat, txt):
        M = len(pat)
        N = len(txt)
        lps = [0] * M
        j = 0
        computeLPSArray(pat, M, lps)
        i = 0
        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1
            if j == M:
                global index_of_optr
                index_of_optr = i - j
                j = lps[j - 1]
                return index_of_optr
            elif i < N and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

    def computeLPSArray(pat, M, lps):
        len = 0
        lps[0]
        i = 1
        while i < M:
            if pat[i] == pat[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                if len != 0:
                    len = lps[len - 1]
                else:
                    lps[i] = 0
                    i += 1

    # txt = #string from js goes here
    txt = input_text
    optrs = ["+", "-", "*", "/", "%"]
    for optr in optrs:
        if KMPSearch(optr, txt):
            pat = [optr]
            pat = pat[0]

    def isdigit(num):
        if num.isdigit():
            return num

    KMPSearch(pat, txt)

    def seperator():
        num1 = txt[:index_of_optr]
        num2 = txt[index_of_optr + 1 :]
        return num1, num2

    num1, num2 = seperator()

    def toInt(num):
        num = isdigit(num)
        num = int(num)
        return num

    def isFloat(num):
        for i in num:
            if KMPSearch(".", num):
                return True

    def num_con(num1, num2):
        if isFloat(num1) or isFloat(num2):
            num1 = float(num1)
            num2 = float(num2)
        else:
            num1 = toInt(num1)
            num2 = toInt(num2)

        return num1, num2

    num1, num2 = num_con(num1, num2)

    def calculate(num1, num2, pat):
        if pat == "+":
            num3 = num1 + num2
            return num3
        if pat == "-":
            num3 = num1 - num2
            return num3
        if pat == "*":
            num3 = num1 * num2
            return num3
        if pat == "/":
            num3 = num1 / num2
            return num3
        if pat == "%":
            num3 = num1 % num2
            return num3

    Ans = calculate(num1, num2, pat)
    Ans = str(Ans)
    return Ans
    # result string is stored in ans variable return the ans variable to js


ans = Result_func("18.988+11.9")
print(ans)

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    j = 0
    computeLPSArray(pat, M, lps)
    i = 0
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            global index_of_optr
            index_of_optr = i - j
            j = lps[j - 1]
            return index_of_optr
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def computeLPSArray(pat, M, lps):
    len = 0
    lps[0]
    i = 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


def isdigit(num):
    if num.isdigit():
        return num


def seperator(txt):
    num1 = txt[:index_of_optr]
    num2 = txt[index_of_optr + 1 :]
    return num1, num2


def toInt(num):
    num = isdigit(num)
    num = int(num)
    return num


def isFloat(num):
    for i in num:
        if KMPSearch(".", num):
            return True


def num_con(num1, num2):
    if isFloat(num1) or isFloat(num2):
        num1 = float(num1)
        num2 = float(num2)
    else:
        num1 = toInt(num1)
        num2 = toInt(num2)
    return num1, num2


def calculate(num1, num2, pat):
    if pat == "+":
        num3 = num1 + num2
        return num3
    if pat == "-":
        num3 = num1 - num2
        return num3
    if pat == "*":
        num3 = num1 * num2
        return num3
    if pat == "/":
        num3 = num1 / num2
        return num3
    if pat == "%":
        num3 = num1 % num2
        return num3


def result_func(input_text):
    # txt = #string from js goes here
    txt = input_text
    optrs = ["+", "-", "*", "/", "%"]
    for optr in optrs:
        if KMPSearch(optr, txt):
            pat = [optr]
            pat = pat[0]

    num1, num2 = seperator(txt)

    KMPSearch(pat, txt)

    num1, num2 = num_con(num1, num2)

    Ans = calculate(num1, num2, pat)
    Ans = round(Ans, 14)
    Ans = str(Ans)
    return Ans
    # result string is stored in ans variable return the ans variable to js
