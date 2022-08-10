"""
Flipping an image:
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
"""

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
    for row in image:
        #print(row)
        #print(row[::-1])
        inverted = lambda x: 0 if x == 1 else 1
        result.append(list(map(inverted, row[::-1])))
    return result

print(flippingImage([[1,1,0],[1,0,1],[0,0,0]]))