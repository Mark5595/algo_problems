# Practice Programing Problems
# 1.6 String compression
# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become
# a2blc5a3. If the "compressed" string would not become smaller than the original
# string, your method should return the original string

# String -> String
# to compress a string per description
def str_compress(s):
    pass

assert str_compress("aabcccccaaa") == "a2blc5a3"
assert str_compress("") == ""
# more cases ???

# 1.7 Rotate Matrix
# Given an image represented by an NxN matrix, where each pixel in the image is
# 4 bytes (say an int), write a method to rotate the image by 90 degrees (cw). Can you do this in
# place?

# DATADEF
# A Matrix is a loloInts, [col][row]

# Matrix -> Matrix (in place?)
# To rotate a matrix in place
def rotate_matrix(m):
    pass

assert rotate_matrix([[]]) == [[]]
'''
1 3  --> 2 1
2 4      4 3  I think?
'''
assert rotate_matrix([[1 2] [3 4]]) == [[2 4] [1 3]]
# ...

# 1.8 Zero Martix
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row
# and column are set to 0.

# Matrix -> Matrix
def zero_martix(m):
    pass

assert rotate_matrix([[]]) == [[]]
'''
1 3  --> 2 1
2 4      4 3
'''
assert rotate_matrix([[1 2] [3 4]]) == [[2 4] [1 3]]
'''
1 3  --> 2 0
2 0      0 0
'''
assert rotate_matrix([[1 2] [3 4]]) == [[2 0] [0 0]]
