"""
Flipping an image:
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
"""
# Leetcode Easy: https://leetcode.com/problems/flipping-an-image/

# image = [[1,1,0],[1,0,1],[0,0,0]]
"""
image = 
[
    [1,1,0],
    [1,0,1],
    [0,0,0]
]
After inverting each item in the list using [::-1]
    |
    V
[
    [0,1,1],
    [1,0,1],
    [0,0,0]
]
Using lambda function to change each item in the row to the opposit(1 to 0); Becomes -> 
[
    [1,0,0],
    [0,1,0],
    [1,1,1]
]
"""
#Becomes -> [[1,0,0],[0,1,0],[1,1,1]]



def flippingImage(image):
    result = []
    inverted = lambda x: 0 if x == 1 else 1
    for row in image:
        result.append(list(map(inverted, row[::-1])))
    return result

def flipAndInvertAnImage(image):
    result = []
    for row in image:
        row = row[::-1] #reversing the elements in the row
        invertedRow = [] #for storing the inverted row
        for item in row:    #going through the elements in each row
            if item == 1:   #checking and replacing 1 with 0 (inverting the elements)
                item = 0
            else:
                item = 1
            invertedRow.append(item) #adding the inverted item to the invertedRow list
        result.append(invertedRow) #adding the list of inverted row into the result
    return result

print(flippingImage([[1,1,0],[1,0,1],[0,0,0]]))
print(flipAndInvertAnImage([[1,1,0],[1,0,1],[0,0,0]]))