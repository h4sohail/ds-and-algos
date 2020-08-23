# given an NxN matrix rotate it by 90 degrees
# we can turn each row to a col, aka take the transpose of the matrix

matrix = [[1,2,3], [4,5,6], [7,8,9]]

def rotate(matrix):
    return list(zip(*matrix))[::-1]

