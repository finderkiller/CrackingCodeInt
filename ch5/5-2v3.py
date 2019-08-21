#! /usr/bin/python3
import sys

def sol_shift_by_1(value):
    if (value <= 0 or value >= 1):
        return ""
    ret = "."
    while(value > 0):
        if (len(ret) > 32):
            return ""
        value = value * 2
        if (value >= 1):
            ret += str(1)
            value = value - 1
        else:
            ret += str(0)
    return ret

def sol_divided(value):
    if value <=0 or value >=1:
        return ""
    frac = 0.5
    ret = "0."
    while value >0:
        if len(ret) >= 34:
            return ""
        if value > frac:
            value -= frac
            ret += "1"
        else:
            ret += "0"
        frac /= 2
    return ret
    

def main(argv):
    print(sol_shift_by_1(float(argv[1])))
    print(sol_divided(float(argv[1])))

if __name__ == "__main__":
    main(sys.argv)
