#  Given an image represented by an NxN matrix, where each pixel in the image is 4
#  bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


def rotate(matrix):
    n = len(matrix)
    rotated_matrix = [[None for x in range(n)] for y in range(n)]
    for row in range(n):
        for col in range(n):
            rotated_matrix[n - 1 - col][row] = matrix[row][col]
    return rotated_matrix


if __name__ == "__main__":
    print(rotate([["a", "b"], ["c", "d"]]))
    print(rotate([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]))
    print(rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))

