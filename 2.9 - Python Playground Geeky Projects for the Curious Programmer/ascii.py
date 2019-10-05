# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:05:53 2019

@author: Maxence
"""

import sys, random, argparse
import numpy as np
import math
from PIL import Image

# grayscale level values from:
# http://paulbourke.net/dataformats/asciiart/

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 10 levels of gray
gscale2 = '@%#*+=-:. '

def getAverageL(image):
    '''
    Given PIL image, return average value of grayscale value
    '''
    # Get image as numpy array
    im = np.array(image)
    # Get the dimensions
    w, h = im.shape
    # Get the average
    return np.average(im.reshape(w*h))

def covertImageToAscii(fileName, cols, scale, moreLevels):
    '''
    Given Image and dimensions (rows, cols), returns an m*n list of Images
    '''
    # Declare globals
    global gscale1, gscale2
    # Open image and convert to grayscale
    image = Image.open(fileName).convert('L')
    # Store the image dimensions
    W, H = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (W, H))
    # Compute tile width
    w = W/cols
    # Compute tile height based on the aspect ratio and scale of the font
    h = w/scale
    # Compute number of rows to use in the final grid
    rows = int(H/h)
    
    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))
    
    # Check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)
    
    # An ASCII image is a list of character strings
    aimg = []
    # Generate the list of tile dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
        # Correct the last tile
        if j == rows-1:
            y2 = H
        # Append an empty string
        aimg.append("")
        for i in range(cols):
            # Crop the image to fit the tile
            x1 = int(i*w)
            x2 = int((i+1)*w)
            # Correct the last tile
            if i == cols-1:
                x2 = W
            # Crop the image to extract the tile into another Image object
            img = image.crop((x1, y1, x2, y2))
            # Get the average luminance
            avg = int(getAverageL(img))
            # Look up the ASCII character for grayscale value (avg)
            if moreLevels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]
            # Append the ASCII character to the string
            aimg[j] += gsval
        
    # Return text image
    return aimg

# main() function
def main():
    # Create parser
    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)
    # Add expected arguments
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels', dest='moreLevels', action='store_true')
    
    # Parse arguments
    args = parser.parse_args()
    
    imgFile = args.imgFile
    # Set output file
    outFile = 'out.txt'
    if args.outFile:
        outFile = args.outFile
    # Set scale default as 0.43, wich suits a Courier font
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
    #+ Set cols
    cols = 80
    if args.cols:
        cols = int(args.cols)
    print('generating ASCII art...')
    # Convert image to ASCII text
    aimg = covertImageToAscii(imgFile, cols, scale, args.moreLevels)
    
    # Open a new text file
    f = open(outFile, 'w')
    # Write each string in the list to the new file
    for row in aimg:
        f.write(row + '\n')
    # Clean up
    f.close()
    print("ASCII art written to %s" % outFile)

# Call main
if __name__ == '__main__':
    main()