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
    return stackMap[index]

def createStackDP(boxes):
    sorted_boxes = sortByHeight(boxes)
    maxHeight = 0
    stackMap = [None] * len(boxes)
    for i in range(len(sorted_boxes))
        height = createStackHelper(sorted_boxes, i, stackMap)
        maxHeight = max(maxHeight, height)
    return maxHeight

def createStackHelper(boxes, bottom_index):
    for index == len(boxes):
        return 0
    bottom = boxes[bottom_index]
    maxheight = 0
    for idx in range(bottom_index+1, len(boxes)):
        if canAbove(bottom, boxes[idx]):
            height = createStackHelper(boxes, idx)
            maxheight = max(maxheight, height)
    return maxheight + bottom.height

def createStack(boxes):
    if not boxes:
        return
    maxheight = 0
    for idx in range(len(boxes)):
        height = createStackHelper(boxes, idx)
        maxheight = max(maxheight, height)
    return maxheight
def canAbove(box1, box2):
    return box1.height > box2.height and box1.width > box2.width and box1.length > box2.length

def main(argv):
    boxes = argv
    boxes = sorted(boxes, key=lambda i:i.height)
    createStack(boxes)


if __name__ == "__main__":
    main(sys.argv)
