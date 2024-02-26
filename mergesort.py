import time



def merge_sort(data, drawData, timeTick):
    merge_sort_algorithm(data, 0, len(data) - 1, drawData, timeTick)




def merge_sort_algorithm(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_algorithm(data, left, middle, drawData, timeTick)
        merge_sort_algorithm(data, middle + 1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)


def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, colorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    leftside = data[left:middle+1]
    rightside = data[middle+1 : right+1]

    leftIndex = rightIndex = 0

    for index in range(left, right):
        if leftIndex < len(leftside) and rightIndex < len(rightside):
            if leftside[leftIndex] <= rightside[rightIndex]:
                data[index] = leftside[leftIndex]
                leftIndex += 1
            else:
                data[index] = rightside[rightIndex]
                rightIndex += 1
        elif leftIndex < len(leftside):
            data[index] = leftside[leftIndex]
            leftIndex += 1
        else:
            data[index] = rightside[rightIndex]
            rightIndex += 1

    drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)        

def colorArray(length, left, middle, right):
    colorArray = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("orange")
        else:
            colorArray.append("white")
    return colorArray