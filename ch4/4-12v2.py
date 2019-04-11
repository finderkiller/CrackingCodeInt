#! /usr/local/bin/python3
import sys
from basic_tree_node import *

def sol2_hash(node, targetSum):
    if (node == None):
        return 0
    sum_count_dict = {}
    return iterate_node(node, targetSum, 0, sum_count_dict)

def iterate_node(node, targetSum, currentSum, sum_count_dict):
    if (node == None):
        return 0
    currentSum += node.value
    diff = targetSum - currentSum
    path = sum_count_dict.get(diff, 0)
    if (currentSum == targetSum):
        path += 1
    Increment_hash(sum_count_dict, currentSum, 1)
    path += iterate_node(node.left, targetSum, currentSum, sum_count_dict)
    path += iterate_node(node.right, targetSum, currentSum, sum_count_dict)
    Increment_hash(sum_count_dict, key, -1)
    return path

def Increment_hash(sum_count_dict, key, delta):
    newCount = sum_count_dict.get(key, 0) + delta
    if (newCount == 0):
        sum_count_dict.pop(key) #Remove when zero to reduce space usage
    else:
        sum_count_dict[key] = newCount  

def sol1_brute(node, targetSum):
    if (node == None):
        return 0
    rootCount = count_sum_path(node, targetSum, 0)
    leftCount = sol1_brute(node.left, targetSum)
    rightCount = sol1_brute(node.right, targetSum)

    return rootCount + leftCount + rightCount

def count_sum_path(node, targetSum, currentSum):
    if (node == None):
        return 0
    totalPath = 0
    currentSum += node.value
    if (currentSum == targetSum):
        totalPath += 1
    totalPath += count_sum_path(node.left, targetSum, currentSum)
    totalPath += count_sum_path(node.right, targetSum, currentSum)
    
    return totalPath


def main(argv):
    input = []
    for value in argv[2].split(','):
        input.append(int(value))
    root = build_tree_node(input)
    count = sol1_brute(root, int(argv[1]))

if __name__ == "__main__":
    main(sys.argv)