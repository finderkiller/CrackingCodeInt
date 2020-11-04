#! /usr/bin/python3
import sys

def merge(a, b, counta, countb):
  total_idx = len(a) - 1
  idx_a = counta - 1
  idx_b = countb - 1
  while idx_a >=0 or idx_b >=0:
    if idx_a < 0:
      a[total_idx] = b[idx_b]
      idx_b -= 1
    elif idx_b < 0:
      break
    elif a[idx_a] >= b[idx_b]:
      a[total_idx] = a[idx_a]
      idx_a -= 1
    else:
      a[total_idx] = b[idx_b]
      idx_b -= 1
    total_idx -= 1


def main(argv):
    counta = 0
    countb = 0
    for value in argv[1].split(','):
        counta += 1
    for value in argv[2].split(','):
        countb += 1

    a = [None] * (counta + countb)
    b = [None] * countb
    for idx, value in enumerate(argv[1].split(',')):
        a[idx] = value
    for idx, value in enumerate(argv[2].split(',')):
        b[idx] = value

    merge(a, b, counta, countb)
    print(a)



if __name__ == "__main__":
    main(sys.argv)
