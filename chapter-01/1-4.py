# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A
# palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of
# letters. The palindrome does not need to be limited to just dictionary words.


def check_palindrome_permutation(string):
    count = {}
    odd_counter = 0
    for char in string.replace(" ", ""):
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    for char_count in count.values():
        odd_counter += char_count % 2
        if odd_counter > 1:
            return False
    return True


if __name__ == "__main__":
    print(check_palindrome_permutation("taco cta"))
    print(check_palindrome_permutation("tao cat"))
