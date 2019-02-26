#! /usr/bin/python3
import sys

def createStackDPHelper(boxes, index, stackMap):
    if (index == len(boxes)):
        return 0
    if (stackMap[index] != None):
        return stackMap[index]
    maxHeight = 0
    bottomBox = boxes[index]
    for i in range(index + 1, len(boxes)):
        if (canAbove(boxes[i], bottomBox)):
            height = createStackDpHelper(boxes, i, stackMap)
            maxHeight = max(height, maxHeight)

    stackMap[index] = maxHeight + bottomBox.height
    return return stackMap[index]

def createStackDP(boxes):
    sorted_boxes = sortByHeight(boxes)
    maxHeight = 0
    stackMap = [None] * len(boxes)
    for i in range(len(sorted_boxes))
        height = createStackHelper(sorted_boxes, i, stackMap)
        maxHeight = max(maxHeight, height)
    return maxHeight

def createStackHelper(boxes, index):
    if (index == len(boxes)):
        return 0
    maxHeight = 0
    bottomBox = boxes[index]
    for i in range(index + 1, len(boxes)):
        if (canAbove(boxes[i], bottomBox)):
            height = createStackHelper(boxes, i)
            maxHeight = max(height, maxHeight)
    return maxHeight + bottomBox.height

def createStack(boxes):
    sorted_boxes = sortByHeight(boxes)
    maxHeight = 0
    for i in range(len(sorted_boxes))
        height = createStackHelper(sorted_boxes, i)
        maxHeight = max(maxHeight, height)
    return maxHeight

def main(argv):
    createStack(boxes)


if __name__ == "__main__":
    main(sys.argv)
