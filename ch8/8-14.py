#! /usr/bin/python3
import sys

def countEval(expression, result):
    if len(expression) == 0:
        return 0
    if len(expression) == 1:
        return 1 if bool(expression) == result else 0
    ways = 0
    for idx in range(1, len(expression), 2):
        left = expression[:idx]
        right = expression[idx+1:]
        leftTrue = countEval(left, True)
        leftFalse = countEval(left, False)
        rightTrue = countEval(right, True)
        rightFalse = countEval(right, False)

        total = (leftTrue + leftFalse) * (rightTrue + rightFalse)
        totalTrue = 0
        if expression[idx] == '^':
            totalTrue = leftTrue * rightFalse + leftFalse * rightTrue
        if expression[idx] == '&':
            totalTrue = leftTrue * rightTrue
        if expression[idx] == '|':
            totalTrue = leftTrue * rightTrue + leftTrue * rightFalse + leftFalse * rightTrue

        subways = totalTrue if result else total - totalTrue
        ways += subways
    return ways

def countEvalMem(expression, result, table):
    if len(expression) == 0:
        return 0
    if len(expression) == 1:
        return 1 if bool(expression) == result else 0
    if (str(result)+expression) in table:
        return table[str(result)+expression]

    ways = 0
    for idx in range(1, len(expression), 2):
        left = expression[:idx]
        right = expression[idx+1:]
        leftTrue = countEval(left, True)
        leftFalse = countEval(left, False)
        rightTrue = countEval(right, True)
        rightFalse = countEval(right, False)

        total = (leftTrue + leftFalse) * (rightTrue + rightFalse)
        totalTrue = 0
        if expression[idx] == '^':
            totalTrue = leftTrue * rightFalse + leftFalse * rightTrue
        if expression[idx] == '&':
            totalTrue = leftTrue * rightTrue
        if expression[idx] == '|':
            totalTrue = leftTrue * rightTrue + leftTrue * rightFalse + leftFalse * rightTrue

        subways = totalTrue if result else total - totalTrue
        ways += subways
    table[str(result)+expression] = ways
    return ways

def main(argv):
    expression = argv[1]
    result = bool(argv[2])
    table = {}
    print(countEval(expression, result))
    print(countEvalMem(expression, result, table))


if __name__ == "__main__":
    main(sys.argv)
