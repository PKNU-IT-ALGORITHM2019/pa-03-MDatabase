import random
import timeit
import sys

sys.setrecursionlimit(15000)

def swap(data, i, j):
    data[i], data[j] = data[j], data[i]

def bubbleSort(data):
    for size in reversed(range(len(data))):
        for i in range(size):
            if data[i] > data[i+1]:
                swap(data, i, i+1)

def selectionSort(data):
    for size in reversed(range(len(data))):
        max_i = 0
        for i in range(1, 1+size):
            if data[i] > data[max_i]:
                max_i = i
        swap(data, max_i, size)

def insertionSort(data):
    for size in range(1, len(data)):
        val = data[size]
        i = size
        while i > 0 and data[i-1] > val:
            data[i] = data[i-1]
            i -= 1
        data[i] = val

def mergeSort(data):
    if len(data) > 1:
        mid = len(data)//2
        ldata, rdata = data[:mid], data[mid:]
        mergeSort(ldata)
        mergeSort(rdata)

        li, ri, i = 0, 0, 0
        while li < len(ldata) and ri < len(rdata):
            if ldata[li] < rdata[ri]:
                data[i] = ldata[li]
                li += 1
            else:
                data[i] = rdata[ri]
                ri += 1
            i += 1
        data[i:] = ldata[li:] if li != len(ldata) else rdata[ri:]


def quick_sorted(arr,pivot_temp):
    if pivot_temp is "last":
        if len(arr)<=1:
            return arr
        pivot_num=len(arr)-1
    elif pivot_temp is "random":
        if len(arr) <= 1:
            return arr
        pivot_num=random.randrange(0,len(arr))
    elif pivot_temp is "middle":
        pivot_num=int((len(arr)-1)/2)

    if len(arr) > 1:
        pivot = arr[pivot_num]
        left, mid, right = [], [], []
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
        mid.append(pivot)
        return quick_sorted(left,pivot_temp) + mid + quick_sorted(right,pivot_temp)
    else:
        return arr

Array1_RD=[]
Array2_RD=[]
Array3_RD=[]
Array1_RV=[]
Array2_RV=[]
Array3_RV=[]

for i in range(1000):
    Array1_RV.append(1000-i)
    Array1_RD.append(random.randrange(1,1001))
for i in range(10000):
    Array2_RV.append(10000-i)
    Array2_RD.append(random.randrange(1,10001))
for i in range(100000):
    Array3_RV.append(100000-i)
    Array3_RD.append(random.randrange(1,100001))

    Array_temp=[]
def printresult(Method,array):
    Array_temp=list(array)
    start = timeit.default_timer()
    Method(Array_temp)
    end=timeit.default_timer()
    sys.stdout.write(str(round(end-start,3)))
    sys.stdout.write("\t\t")

def Qprintresult(Method,array,pivot):
    Array_temp=list(array)
    start = timeit.default_timer()
    Method(Array_temp,pivot)
    end=timeit.default_timer()
    sys.stdout.write(str(round(end-start,3)))
    sys.stdout.write("\t\t")


print("\t\tRandom1000\tReverse1000\tRandom10000\tReverse10000\tRandom100000\tReverse100000")
sys.stdout.write("Bubble\t\t")    
printresult(bubbleSort,Array1_RD)
printresult(bubbleSort,Array1_RV)
printresult(bubbleSort,Array2_RD)
printresult(bubbleSort,Array2_RV)
#printresult(bubbleSort,Array3_RV)
#printresult(bubbleSort,Array3_RV)
print()

sys.stdout.write("Selection\t")
printresult(selectionSort,Array1_RD)
printresult(selectionSort,Array1_RV)
printresult(selectionSort,Array2_RD)
printresult(selectionSort,Array2_RV)
#printresult(selectionSort,Array3_RD)
#printresult(selectionSort,Array3_RV)
print()


sys.stdout.write("Insertion\t")
printresult(insertionSort,Array1_RD)
printresult(insertionSort,Array1_RV)
printresult(insertionSort,Array2_RD)
printresult(insertionSort,Array2_RV)
#printresult(insertionSort,Array3_RD)
#printresult(insertionSort,Array3_RV)
print()

sys.stdout.write("Merge\t\t")
printresult(mergeSort,Array1_RD)
printresult(mergeSort,Array1_RV)
printresult(mergeSort,Array2_RD)
printresult(mergeSort,Array2_RV)
printresult(mergeSort,Array3_RD)
printresult(mergeSort,Array3_RV)
print()

sys.stdout.write("Quick1\t\t")
Qprintresult(quick_sorted,Array1_RD,"last")
Qprintresult(quick_sorted,Array1_RV,"last")
Qprintresult(quick_sorted,Array2_RD,"last")
#Qprintresult(quick_sorted,Array2_RV,"last") # 메모리에러로 실행불가능
sys.stdout.write("\t\t")
Qprintresult(quick_sorted,Array3_RD,"last")
#Qprintresult(quick_sorted,Array3_RD,"last")
print()

sys.stdout.write("Quick2\t\t")
Qprintresult(quick_sorted,Array1_RD,"middle")
Qprintresult(quick_sorted,Array1_RV,"middle")
Qprintresult(quick_sorted,Array2_RD,"middle")
Qprintresult(quick_sorted,Array2_RV,"middle")
Qprintresult(quick_sorted,Array3_RD,"middle")
Qprintresult(quick_sorted,Array3_RD,"middle")
print()

sys.stdout.write("Quick3\t\t")
Qprintresult(quick_sorted,Array1_RD,"random")
Qprintresult(quick_sorted,Array1_RV,"random")
Qprintresult(quick_sorted,Array2_RD,"random")
Qprintresult(quick_sorted,Array2_RV,"random")
Qprintresult(quick_sorted,Array3_RD,"random")
Qprintresult(quick_sorted,Array3_RV,"random")
print()
