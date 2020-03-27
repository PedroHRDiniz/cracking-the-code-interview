# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?


def is_unique(str):
    chars = {}
    for char in str:
        if char in chars:
            return False
        else:
            chars[char] = True
    return True


if __name__ == "__main__":
    print(is_unique("aba"))
    print(is_unique("ab"))
