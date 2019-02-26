#! /usr/bin/python3
import sys
from bitstring import BitArray

a = []

def main(array):
    bs = BitArray(32000)
    for value in array:
        index = value - 1
        if (bs[index] == 1):
            print(value)
            continue
        bs[index] = 1



if __name__ == "__main__":
    main(a)
