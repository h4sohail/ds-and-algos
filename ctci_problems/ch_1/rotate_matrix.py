# given an NxN matrix rotate it by 90 degrees
# # we can turn each row to a col, aka take the transpose of the matrix

def rotate(matrix):
    return list(zip(*matrix))[::-1]

