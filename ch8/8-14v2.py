#! /usr/bin/python3
import sys

def countEval(expression, result):
    if not expression:
        return 0
    if len(expression) == 1:
        return 1 if bool(expression) == result else 0
    ways = 0
    for idx in range(1, len(expression, 2):
        left = expression[:idx]
        right = expression[idx+1:]
        left_true = countEval(left, True)
        left_false = countEval(left, False)
        right_true = countEval(right, True)
        right_false = countEval(right, False)

        total_eval = (left_true + left_false) * (right_true + right_false)
        operator = expression[idx]
        if operator == "&":
            total_true = left_true * right_true
        elif operator == "|":
            total_true = left_true * right_true + left_true * right_false + left_false * right_true
        else:
            total_true = left_true * right_false + left_false * right_true
        total_false = total_eval - total_true
        ways += total_true if result else total_false
    return ways
        
    

def countEvalMem(expression, result, table):
    if not expression:
        return 0
    if len(expression) == 1:
        return 1 if bool(expression) == result else 0
    if str(result)+expression in table:
        return table[(str(result)+expression)]
    ways = 0
    for idx in range(1, len(expression, 2):
        left = expression[:idx]
        right = expression[idx+1:]
        left_true = countEval(left, True)
        left_false = countEval(left, False)
        right_true = countEval(right, True)
        right_false = countEval(right, False)

        total_eval = (left_true + left_false) * (right_true + right_false)
        operator = expression[idx]
        if operator == "&":
            total_true = left_true * right_true
        elif operator == "|":
            total_true = left_true * right_true + left_true * right_false + left_false * right_true
        else:
            total_true = left_true * right_false + left_false * right_true
        total_false = total_eval - total_true
        ways += total_true if result else total_false
    table[(str(result)+expression) = ways
    return ways

def main(argv):
    expression = argv[1]
    result = bool(argv[2])
    table = {}
    print(countEval(expression, result))
    print(countEvalMem(expression, result, table))


if __name__ == "__main__":
    main(sys.argv)
