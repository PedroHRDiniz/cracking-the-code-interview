# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).


def compress(string):
    compressed_string = ""
    current_char = string[0]
    count = 1
    for char in string[1:]:
        if current_char == char:
            count += 1
        else:
            compressed_string += current_char + str(count)
            current_char = char
            count = 1
    compressed_string += current_char + str(count)
    if len(string) <= len(compressed_string):
        return string
    else:
        return compressed_string


if __name__ == "__main__":
    print(compress("aabcccccaaa"))
    print(compress("abc"))
