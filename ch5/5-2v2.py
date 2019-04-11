#! /usr/local/bin/python3
import sys

def sol1_shift(value):
    if (value >=1 or value <= 0):
        return ""
    output = "."
    while(value > 0):
        if(len(output) > 33):
            return ""
        num = value * 2
        if (num >= 1):
            output += str(1)
            value = num - 1
        else:
            output += str(0)
            value = num
    return output

def sol2_divide(value):
    if (value >=1 or value <= 0):
        return ""
    output = "."
    frac = 0.5
    while(value > 0):
        if (len(output) > 33):
            return ""
        if value >= frac:
            output += str(1)
            value = value - frac
        else:
            output += str(0)
        frac /= 2
    return output



def main(argv):
    print(sol1_shift(float(argv[1])))
    print(sol2_divide(float(argv[1])))

if __name__ == "__main__":
    main(sys.argv)