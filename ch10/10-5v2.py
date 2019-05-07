#! /usr/bin/python3
import sys

def Search(input, value, first, last):
    if (last < first):
        return -1
    mid = (first+last)//2
    if (input[mid] == ""):
        right = mid + 1
        left = mid - 1
        while(True):
            if (right > last and left < first):
                return -1
            elif (right <= last and input[right] != ""):
                mid = right
                break
            elif (left >= first and input[left] != ""):
                mid = left
                break
            left -= 1
            right += 1

    if input[mid] == value:
        return mid
    elif input[mid] > value:
        return Search(input, value, first, mid-1)
    else:
        return Search(input, value, mid+1, last)
    return -1



def main(argv):
    input=[]
    for string in argv[1].split(','):
        input.append(string)
    print(Search(input, argv[2], 0, len(input)-1))

if __name__ == "__main__":
    main(sys.argv)
