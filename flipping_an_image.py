"""
Flipping an image:
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
"""

# image = [[1,1,0],[1,0,1],[0,0,0]]
#Becomes -> [[1,0,0],[0,1,0],[1,1,1]]

from operator import inv


def flippingImage(image):
    for row in image:
        #print(row)
        inverted = lambda x: 0 if x == 1 else 1
        result = (list(map(inverted, item)) for item in row[::-1])
        return result

print(flippingImage([[1,1,0],[1,0,1],[0,0,0]]))