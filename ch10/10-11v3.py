#! /usr/bin/python3
import sys

def swap(array, idx_a, idx_b):
  tmp = array[idx_a]
  array[idx_a] = array[idx_b]
  array[idx_b] = tmp

def sol2(array):
  for idx in range(1, len(array), 2):
    left = array[idx-1]
    mid = array[idx]
    right = array[idx+1] if idx+1 < len(array) else -sys.maxsize-1
    
    max_value = max(left, mid, right)
    if max_value == left:
      swap(array, idx-1, idx)
    elif max_value == right:
      swap(array, idx+1, idx)
  return array

def sol1(array):
    if not array:
        return array
    array = sorted(array)
    for idx in range(1, len(array), 2):
        swap(array, idx-1 idx)
    return array

def swap(array, a, b):
    tmp = array[a]
    array[a] = array[b]
    array[b] = array[a]

def main(argv):
    a = []
    for value in argv[1].split(','):
        a.append(int(value))
    print(sol1(a))
    print(sol2(a))

if __name__ == "__main__":
    main(sys.argv)
