#! /usr/bin/python3
import sys
from bitstring import BitArray

def sol(i, j):
    n = int('1111111', 2)
    m = int('111', 2)
    allone = -1
    left = allone << j+1
    right = (1 << i) - 1
    mask = left | right
    print(mask)
    print(bin(mask))
    n_clear = n & mask
    print(bin(n_clear))
    m_shift = m << i
    print(bin(m_shift))
    return bin(n_clear | m_shift)

def main(argv):
    print(sol(int(argv[1]), int(argv[2])))

if __name__ == "__main__":
    main(sys.argv)
