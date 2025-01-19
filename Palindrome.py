def isPalindrome(string):
    data = list(string)

    start_index = 0
    end_index = len(data) - 1

    while end_index > start_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index += 1
        end_index -= 1

    data = "".join(data)

    if data == string:
        print("the string is a palindrome")
    else:
        print("the string is not a palindrome")


isPalindrome("nitin")
