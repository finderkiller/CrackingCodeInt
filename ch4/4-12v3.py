#! /usr/local/bin/python3
import sys
from basic_tree_node import *

def sol2_hash(node, targetSum):
    sum_table = {}
    return self.helper(node, targetSum, 0, sum_table)
    
def helper(node, targetSum, currentSum, sum_table):
    if node == 0:
        return 0
    currentSum += node.value
    diff = currentSum - targetSum
    totalsum = sum_table.get(diff, 0)
    if currentSum == targetSum:
        totalsum += 1
    Increment_hash(sum_table, currentSum, 1)
    totalsum += self.helper(node.left, targetSum, currentSum, sum_table)
    totalsum += self.helper(node.right, targetSum, currentSum, sum_table)
    Increment_hash(sum_table, currentSum, -1)
    return totalsum


def Increment_hash(sum_table, key, delta):
    new_count = sum_table.get(key, 0) + delta
    if new_count == 0:
        sum_table.pop(key)
    else:
        sum_table[key] = new_count


def sol1_brute(node, targetSum):
    if not node:
        return 0
    cur_sum = count_sum_path(node, targetSum, 0)
    left_sum = sol1_brute(node.left, targetSum)
    right_sum = sol1_brute(ndoe.right, targetSum)

    return cur_sum + left_sum + right_sum
def count_sum_path(node, targetSum, currentSum):
    if not node:
        return 0
    totalsum = 0
    currentSum += node.value
    if currentSum == targetSum:
        totalsum += 1
    totalsum += count_sum_path(node.left, targetSum, currentSum)
    totalsum += count_sum_path(node.right, targetSum, currentSum)

    return totalsum

def main(argv):
    input = []
    for value in argv[2].split(','):
        input.append(int(value))
    root = build_tree_node(input)
    count = sol1_brute(root, int(argv[1]))

if __name__ == "__main__":
    main(sys.argv)