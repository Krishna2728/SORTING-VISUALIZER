import time


def partition(data , head , tail ,drawData , timetick):
    border = head
    pivot = data[tail]

    drawData(data , getcolorArray(len(data) , head , tail , border , border  ))
    time.sleep(timetick)

    for j in range(head , tail):
        if data[j]<pivot:
            drawData(data , getcolorArray(len(data) , head , tail , border , j , True  ))
            time.sleep(timetick)

            data[border] , data[j] = data[j] , data[border]
            border += 1

        drawData(data , getcolorArray(len(data) , head , tail , border , j  ))
        time.sleep(timetick)

    drawData(data , getcolorArray(len(data) , head , tail , border , tail , True  ))
    time.sleep(timetick)
    data[border] , data[tail] = data[tail] , data[border]
    return border

def quick_sort(data , head , tail , drawData , timetick):

    if head<tail:
        partitionidx = partition(data , head , tail , drawData , timetick)
        quick_sort(data , head , partitionidx-1 , drawData , timetick )
        quick_sort(data , partitionidx+1 , tail , drawData , timetick)

def getcolorArray(datalen , head , tail , border ,curridx , isswapping = False):
    colorArray = []

    for i in range(datalen):
        if i >=head and i <=tail:
            colorArray.append('grey')
        else:
            colorArray.append('white')

        if i==tail:
            colorArray[i] = 'blue'
        elif i ==border:
            colorArray[i] = 'red'
        elif i ==curridx:
            colorArray[i] = 'yellow'

        if isswapping:
            if i ==border or i==curridx:
                colorArray[i] = 'green'
    return colorArray