#! /usr/bin/python3
import sys

def genParen(remainder):
    ret = set()
    if (remainder == 0):
        ret.add("")
        return ret
    parens = genParen(remainder - 1)
    for paren in parens:
        ret.add("()" + paren)
        for idx, val in enumerate(paren):
            if val == "(":
                ret.add(paren[:idx+1] + "()" + paren[idx+1:])
    return ret

def main(argv):
    print(genParen(int(argv[1])))

if __name__ == "__main__":
    main(sys.argv)
