#! /usr/bin/python3
import sys

def createStackDP(boxes):
    height_table = [None] * len(boxes)
    sorted_boxes = boxes.sort(key=takeHeight)
    maxHeight = 0
    for idx in range(len(sorted_boxes)):
        height = createStackHelper(boxes, idx, height_table)
        maxHeight = max(height, maxHeight)
    return maxHeight

def createStackDPHelper(boxes, bottomIdx, height_table):
    if(bottomIdx == len(boxes)):
        return 0
    if height_table[bottomIdx] != None:
        return height_table[bottomIdx]

    bottomBox = boxes[bottomIdx]
    maxHeight = 0
    for idx in range(bottomIdx+1, len(boxes)):
        if (canAbove(bottomBox, boxes[idx])):
            height = createStackHelper(boxes, idx, height_table)
            maxHeight = max(height, maxHeight)

    height_table[bottomIdx] = maxHeight + bottomBox.height
    return height_table[bottomIdx]



def createStack(boxes):
    sorted_boxes = boxes.sort(key=takeHeight)
    maxHeight = 0
    for idx in range(len(sorted_boxes)):
        height = createStackHelper(boxes, idx)
        maxHeight = max(height, maxHeight)
    return maxHeight

def createStackHelper(boxes, bottomIdx):
    if (bottomIdx == len(boxes)):
        return 0
    bottomBox = boxes[bottomIdx]
    maxHeight = 0
    for idx in range(bottomIdx+1, len(boxes)):
        if (canAbove(bottomBox, boxes[idx])):
            height = createStackHelper(boxes, idx)
            maxHeight = max(height, maxHeight)

    return maxHeight + bottomBox.height

def canAbove(bottomBox, box):
    return bottomBox.height > box.height and bottomBox.width > box.width and bottomBox.length > box.length

def takeHeight(box):
    return box.height


def main(argv):
    boxes = argv
    createStack(boxes)
    createStackDP(boxes)


if __name__ == "__main__":
    main(sys.argv)
