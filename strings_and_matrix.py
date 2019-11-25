# Practice Programing Problems
# 1.6 String compression
# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become
# a2blc5a3. If the "compressed" string would not become smaller than the original
# string, your method should return the original string

# String -> String
# to compress a string per description
def str_compress(s):
    # loChar -> String
    # does the compression no matter what
    def str_compress_help(loChar):
        if not loChar:
            return ""
        build_str = ""
        while loChar:
            curr = loChar[0]
            count = 0
            #print("--")
            while loChar and curr == loChar[0]:
                #print("curr is", curr)
                loChar.remove(curr)
                count += 1
            build_str += curr
            build_str += str(count)

        return build_str

    compress_str = str_compress_help(list(s))
    if len(s) <= len(compress_str):
        return s
    else: # compress string is smaller than the original
        return compress_str


assert str_compress("aa") == "aa"
assert str_compress("aaa") == "a3"
#print(str_compress("aabcccccaaa"))
assert str_compress("aabcccccaaa") == "a2b1c5a3"
assert str_compress("") == ""
# more cases ???

# 1.7 Rotate Matrix
# Given an image represented by an NxN matrix, where each pixel in the image is
# 4 bytes (say an int), write a method to rotate the image by 90 degrees (cw). Can you do this in
# place?

# DATADEF
# A Matrix is a loloInts, [col][row]

# Matrix Integer -> Matrix (mutated)
# rotates a level of a matrix
def rotate_layer(m, layer):
    #print("before", m)
    for i in range(0, len(m) - 1 - layer * 2):
        # 4 sides to worry about
        # side 1 top upper
        lower = len(m) - 1 - layer
        #print("loweer ", lower)
        top = m[i + layer][layer]
        lft = m[layer][lower - i]
        bot = m[lower - i][lower]
        rht = m[lower][i + layer]
        #print("top ", top, "righ ", rht, "bot ", bot, "lft", lft)
        m[i + layer][layer] = lft
        m[layer][lower - i] = bot #left
        m[lower - i][lower] = rht #bot
        m[lower][i + layer] = top #right
    #print("after", m)
    return m

assert rotate_layer([[1]], 0) == [[1]]
assert rotate_layer([[1, 2], [3, 4]], 0) == [[2, 4], [1, 3]]
assert rotate_layer([[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]], 0) \
                    == [[13,  14, 15, 16], [9, 6, 10, 12], [5, 7, 11, 8], [1, 2, 3, 4]]
assert rotate_layer([[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]], 1) \
                    == [[1, 5, 9, 13], [2, 10, 11, 14], [3, 6, 7, 15], [4, 8, 12, 16]]
                    #[[13, 14, 15, 16], [9, 10, 11, 12], [5, 6, 7, 8], [1, 2, 3, 4]]

def layer_len(m):
    if len(m) == 0:
        return 0
    return int(len(m) / 2)

# Matrix -> Matrix (in place?)
# To rotate a matrix in place
def rotate_matrix(m):
    #print("before", m)
    for i in range(0, layer_len(m)):
        rotate_layer(m, i)
    #print("after", m)
    return m


assert rotate_matrix([[]]) == [[]]
assert rotate_matrix([[1]]) == [[1]]
'''
1 3  --> 2 1
2 4      4 3  I think?
'''
assert rotate_matrix([[1, 2], [3, 4]]) == [[2, 4], [1, 3]]
assert rotate_matrix([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])  \
                    == [[5, 5, 5, 5, 5], [4, 4, 4, 4, 4], [3, 3, 3, 3, 3], [2, 2, 2, 2, 2], [1, 1, 1, 1, 1]]
# ...

'''
1 2 3   - > 7 4 1
4 5 6       8 5 2
7 8 9       9 6 3
'''

# 1.8 Zero Martix
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row
# and column are set to 0.

# Matrix -> Matrix
def zero_martix(m):
    # To do in constaint mem. use the first row and first column as an
    # indicator of all zero
    set_all_zero_row = False
    set_all_zero_col = False

    for i in m[0]:
        if i == 0:
            set_all_zero_col = Fa

    pass

assert rotate_matrix([[]]) == [[]]
'''
1 3  --> 2 1
2 4      4 3
'''
assert rotate_matrix([[1, 2] [3, 4]]) == [[2, 4] [1, 3]]
'''
1 3  --> 2 0
2 0      0 0
'''
assert rotate_matrix([[1, 2] [3, 4]]) == [[2, 0] [0, 0]]
