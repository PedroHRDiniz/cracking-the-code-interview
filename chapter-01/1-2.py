# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.


def check_permutation(str1, str2):
    count = {}
    for char in str1:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    for char in str2:
        if char not in count:
            return False
        else:
            count[char] -= 1
        if count[char] == 0:
            del count[char]
    return len(count) == 0


if __name__ == "__main__":
    print(check_permutation('abac', 'caba'))
    print(check_permutation('abaca', 'caba'))
