# URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)


def urlify(string):
    empty_space = " "
    chars = list(string)
    i = j = len(chars) - 1
    while chars[i] == empty_space:
        i -= 1
    while j != i:
        if chars[i] == empty_space:
            chars[j] = "0"
            chars[j - 1] = "2"
            chars[j - 2] = "%"
            j -= 2
        else:
            chars[j] = chars[i]
        i -= 1
        j -= 1
    return ''.join(chars)


if __name__ == "__main__":
    print(urlify("taco cat  "))
    print(urlify("tao ca t    "))
