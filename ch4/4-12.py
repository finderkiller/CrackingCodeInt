#! /usr/bin/python3
from basic_tree_node import *
import sys

#sol2: time:O(n), traverse n nodes, space:O(logn) in balanced tree, O(n) in the worst case
def sol2_count_path(node, targetSum):
    path_count = {}
    return count_path_using_hash(node, targetSum, 0, path_count)

def count_path_using_hash(node, targetSum, currentSum, path_count):
    if (node == None):
        return 0
    currentSum += node.value
    diff = currentSum - targetSum
    totalPath = path_count.get(diff, 0)
    if (currentSum == targetSum):
        totalPath += 1
    IncrementHash(path_count, currentSum, 1)
    totalPath += count_path_using_hash(node.left, targetSum, currentSum, path_count)
    totalPath += count_path_using_hash(node.right, targetSum, currentSum, path_count)
    IncrementHash(path_count, currentSum, -1)
    return totalPath

def IncrementHash(path_count, key, delta):
    newCount = path_count.get(key, 0) + delta
    if (newCount == 0):
        path_count.pop(key)
    else:
        path_count[key] = newCount

#sol1: time:O(nlogn), n nodes, each node touch logn nodes (depth is logn)
def sol_brute_force(node, targetSum, currentSum, ):
    if (node == None):
        return 0;
    pathSumOnNode = pathWithSumFromNode(node, targetSum, 0)
    pathSumOnLeft = sol_brute_force(node.left, targetSum)
    pathSumOnRight = sol_brute_force(node.right, targetSum)

    return pathSumOnNode + pathSumOnLeft + pathSumOnRight

def pathWithSumFromNode(node, targetSum, currentSum):
    if (node == None):
        return 0
    currentSum += node.value
    totalPath = 0
    if (currentSum == targetSum):
        totalPath += 1
    totalPath += pathWithSumFromNode(node.left, targetSum, currentSum)
    totalPath += pathWithSumFromNode(node.right, targetSum, currentSum)

    return totalPath


def main(argv):
    input = []
    for value in argv[1].split(','):
        input.append(value)

    root = build_tree_node(input)
#    print (sol_brute_force(root, 6))
    print (sol2_count_path(root, 6))


if __name__ == "__main__":
    main(sys.argv)
