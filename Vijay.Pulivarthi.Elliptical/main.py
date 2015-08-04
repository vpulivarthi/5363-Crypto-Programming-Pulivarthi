import argparse
import sys
import curve as c
from fractions import Fraction

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",dest="x1", help="X of point 1")
    parser.add_argument("-y1",dest="y1", help="Y of point 1")
    parser.add_argument("-x2",dest="x2", help="X of point 2")
    parser.add_argument("-y2",dest="y2", help="Y of point 2")

    args = parser.parse_args()

    # Fractions for inputting the fraction in a/b format.
    x1 = Fraction(args.x1)
    x2 = Fraction(args.x2)
    y1 = Fraction(args.y1)
    y2 = Fraction(args.y2)
    a = Fraction(args.a)
    b = Fraction(args.b)

    # Example:
    # python3 program_name.py -x1 2 -y1 3 -x2 -1 -y2 -1 -a 2 -b 1
    c.lineEquation(x1,y1,x2,y2,a,b)

    print("a=",args.a," b=",args.b,"x1=",args.x1," y1=",args.y1," x2=",args.x2," y2=",args.y2)


if __name__ == '__main__':
    main()
