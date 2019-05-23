#! /usr/bin/python3
import sys

#sol1: copy string, space = O(n)
#sol2: in place

def sol_in_place(string, true_length):
    space_count = 0
    for idx in range(true_length):
        if string[idx] == " ":
            space_count += 1
    final_idx = true_length - 1 + space_count * 2

    slist = list(string)
    for str_idx in range(true_length-1, -1, -1):
        if slist[str_idx] == " ":
            slist[final_idx] = "0"
            slist[final_idx - 1] = "2"
            slist[final_idx - 2] = "%"
            final_idx -= 3
        else:
            slist[final_idx] = slist[str_idx]
            final_idx -= 1
    return ''.join(slist)


def main(argv):
    print(sol_in_place(argv[1], int(argv[2])))

if __name__ == "__main__":
    main(sys.argv)
