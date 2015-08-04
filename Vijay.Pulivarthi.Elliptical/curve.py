###############################################
# Name: Vijay Kumar Pulivarthi
# Class: CMPS 5363 Cryptography
# Date: 04 August 2015
# Program 3 - Elliptical Curve Encryption
###############################################

import sys
import numpy as np
import matplotlib.pyplot as plt

def lineEquation(x1,y1,x2,y2,a,b):

        
    # Create two points
    x3 = 0.0 # Initializing
    y3 = 0.0 # Initializing

    if (y1**2 == (x1**3)+(a*x1)+b) and (y2**2 == (x2**3)+(a*x2)+b):

        # Slope(m) of the line
        if (y2 != y1) and (x2 != x1):
            m = (y2-y1)/(x2-x1)
            print ('The slope value m is %f'%m)
        elif (y2 == y1) and (x2 == x1):
            m = (3*(x1**2)+a)/2*(y1)
            print ('The slope value m is %f'%m)
        elif (x2-x1 == 0) or (y2-y1 == 0):
            print('Cannot solve for slope')
        else:
            sys.exit(0)

    else:
        print('Points do not lie on the curve')
        sys.exit(0)

    # Generating the third point (x3,y3)
    x3 = (m**2-x1-x2)
    y3 = (m*(x3-x1))+y1

    # Maixumum value among the 3 points
    maximumValue = max(abs(x1),abs(y1),abs(x2),abs(y2),abs(x3),abs(y3))

    # Height and Width of the plot
    h = maximumValue+2
    w = maximumValue+2

    
    # Name on the graph
    name = plt.annotate("Vijay Pulivarthi", xy=(-w+2 , h-2), xycoords="data",
              va="center", ha="center",
              bbox=dict(boxstyle="round", fc="w"))

    # This creates a mesh grid with values determined by width and height (w,h)
    # of the plot with increments of .0001 (1000j = .0001 or 5j = .05)
    y, x = np.ogrid[-h:h:1000j, -w:w:1000j]

    # Generating a curve on graph
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) + a*x + b ), [0])
        
    
    # Plot the points ('ro' = red, 'bo' = blue, 'yo'=yellow and so on)
    plt.plot(x1, y1,'ro') 

    # Annotate point 1
    plt.annotate('x1,y1', xy=(x1, y1), xytext=(x1+1,y1+1),
        arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3"),
        )
    # Plotting the second point
    plt.plot(x2, y2,'ro')

    # Annotate point 2
    plt.annotate('x2,y2', xy=(x2, y2), xytext=(x2+1,y2+1),
        arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3"),
        )
    

    # Use a contour plot to draw the line (in pink) connecting our point.
    plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('pink'))

    
    # Plotting the third third point
    plt.plot(x3,y3,'yo')


    # Annotate point 3
    plt.annotate('x3,y3', xy=(x3, y3), xytext=(x3+1,y3+1),
        arrowprops=dict(arrowstyle="->",
        connectionstyle="arc3"),
        )
    
    # Show a grid background on our plot
    plt.grid()

    # Show the plot
    plt.show()

