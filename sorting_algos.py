import time

# bubble sort algorithm
def bubbleSort(nums, drawArray, speed):
    swapped = False
    temp = 0
    
    for i in range(len(nums)):
        for j in range(len(nums)-i-1): # compare until we reach sorted part
            if nums[j] > nums[j+1]: # compare side by side elements, swap if left is bigger
                swapped = True
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                # redraw array with current two selected items colored red
                drawArray(nums, ["#EA706C"if i == j or i == j+1 else "#9592F7" for i in range(len(nums))])
                time.sleep(speed)
                
    # if didnt need to be sorted, recolor arrays red
    drawArray(nums, ["#EA706C" for i in range(len(nums))])
    
    if not swapped: #check if array needed to be sorted
        return
    
# merge sort algos
def mergeSort(data, drawdata, speed):
    mergeSort2(data, 0, len(data)-1, drawdata, speed)
    
def mergeSort2(data, left, right, drawdata, speed):
    if left < right:
        middle = (left + right) // 2
        mergeSort2(data, left, middle, drawdata, speed)
        mergeSort2(data, middle+1, right, drawdata, speed)
        merge(data, left, middle, right, drawdata, speed)

def merge(data, left, middle, right, drawdata, speed):
    drawdata(data, color(len(data), left, middle, right))
    time.sleep(speed)

    left_side = data[left:middle+1]
    right_side = data[middle+1:right+1]

    i, j = 0, 0

    for k in range(left, right+1):
        if i < len(left_side) and j < len(right_side):
            if left_side[i] <= right_side[j]:
                data[k] = left_side[i]
                i += 1
            else:
                data[k] = right_side[j]
                j += 1

        elif i < len(left_side):
            data[k] = left_side[i]
            i += 1
        else:
            data[k] = right_side[j]
            j += 1
    
    drawdata(data, ["#EA706C" if x >= left and x <= right else "#9592F7" for x in range(len(data))])
    time.sleep(speed)

def color(lenn, left, middle, right):
    color_list = []

    for i in range(lenn):
        if i >= left and i <= right:
            color_list.append('gray')
            if i <= left and i >= middle:
                color_list.append('gray')
            else:
                color_list.append('gray')
        else:
            color_list.append("#9592F7")

    return color_list
    
# quick sort algos
def quickSort(data, head, tail, drawdata, speed):

    if head < tail:
        partindex = partition(data, head, tail, drawdata, speed)
        
        #left
        quickSort(data, head, partindex-1, drawdata, speed)

        #right
        quickSort(data, partindex+1, tail, drawdata, speed)
    
def partition(data, head, tail, drawdata, speed):
    border = head
    pivot = data[tail]

    drawdata(data, quickSortColor(len(data), head, tail, border, border))
    time.sleep(speed)

    for j in range(head, tail):
        if data[j] < pivot:
            drawdata(data, quickSortColor(len(data), head, tail, border, j, True))
            time.sleep(speed)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawdata(data, quickSortColor(len(data), head, tail, border, j))
        time.sleep(speed)

    drawdata(data, quickSortColor(len(data), head, tail, border, tail, True))
    time.sleep(speed)

    data[border], data[tail] = data[tail], data[border]

    return border

def quickSortColor(datalen, head, tail, border, currindx, isSwaping = False):
    colorarray = []
    for i in range(datalen):
        if i >= head and i <= tail:
            colorarray.append("gray")
        else:
            colorarray.append("#EA706C")

        if i == tail:
            colorarray[i] = 'blue'
        elif i == border:
            colorarray[i] = 'red'
        elif i == currindx:
            colorarray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currindx:
                colorarray[i] = 'green'

    return colorarray
          
# insertion sort algo
def insertionSort(arr, drawArray, speed):
    for i in range(1, len(arr)): # start from unsorted part until end
        j = i 
        while arr[j-1] > arr[j] and j > 0: # compare to previous item, if smaller then swap
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1 # have to go in reverse to compare to every already sorted item
            drawArray(arr, ["#EA706C"if i == j or i == j+1 else "#9592F7" for i in range(len(arr))]) # colors two elements being compared
            time.sleep(speed)
    
# selection sort algo
def selectionSort(nums, size, speed, drawArray):
    
    # iterate until end of array
    for i in range(size):
        minimum = i # min is first index
        
        # iterate through non sorted elements
        for j in range(i+1, size):
            if nums[j] < nums[minimum]:
                minimum = j # if find another smallest, update
                drawArray(nums, ["#EA706C" if i == minimum else "#9592F7" for i in range(len(nums))])
                time.sleep(speed)
        
        nums[i], nums[minimum] = nums[minimum], nums[i]  # swap current with new smallest
        
        drawArray(nums, ["#EA706C" if i == nums[i] else "#9592F7" for i in range(len(nums))])
        time.sleep(speed)
        