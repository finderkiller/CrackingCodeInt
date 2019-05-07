#! /usr/bin/python3
import sys

def sol(input):
    table = {}
    ret = []
    for string in input:
        key = ''.join(sorted(string))
        if key in table:
            table[key].append(string)
        else:
            table[key] = [string]

    for key in table:
        ret.extend(table[key])
    return ret

def main(argv):
    input = []
    for value in argv[1].split(','):
        input.append(value)
    result = sol(input)
    print(result)


if __name__ == "__main__":
    main(sys.argv)
