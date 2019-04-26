#! /usr/bin/python3
import sys

def genParens(value):
    ret = set()
    if (value == 0):
        ret.add("")
        return ret
    parens = genParens(value - 1)
    for paren in parens:
        ret.add("()" + paren)
        for idx, value in enumerate(paren):
            if(value != "("):
                continue
            ret.add(paren[:idx+1] + "()" + paren[idx+1:])
    return ret

def main(argv):
    print(genParens(int(argv[1])))

if __name__ == "__main__":
    main(sys.argv)
