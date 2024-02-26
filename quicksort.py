import time





def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, colorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for i in range(head, tail):
        if(data[i] < pivot):
            drawData(data, colorArray(len(data), head, tail, border, i, True))
            time.sleep(timeTick)
            data[border], data[i] = data[i], data[border]
            border += 1
            drawData(data, colorArray(len(data), head, tail, border, i))
            time.sleep(timeTick)

    drawData(data, colorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)
    data[border], data[tail] = data[tail], data[border]
    return border


def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:

        partitionIndex = partition(data, head, tail, drawData, timeTick)

        #Left partition
        quick_sort(data, head, partitionIndex-1, drawData, timeTick)

        #Right partition
        quick_sort(data, partitionIndex+1, tail, drawData, timeTick)


def colorArray(dataLen, head, tail, border, currIndex, isSwapping = False):
    colorArray = []
    for i in range(dataLen):
        if i >= head and i <= tail:
            colorArray.append("gray")
        else:
            colorArray.append("white")
        
        if i == tail:
            colorArray[i] == "orange"
        elif i == border:
            colorArray[i] == "red"
        elif i == currIndex:
            colorArray[i] == "yellow"

        if isSwapping:
            if i == border or i == currIndex:
                colorArray[i] = "green"
    return colorArray