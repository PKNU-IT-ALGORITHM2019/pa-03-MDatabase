import random
import timeit
import sys

sys.setrecursionlimit(10000000)

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

#def Middle(data, lmark, rmark):
#    pivot_val = data[int((lmark+rmark)/2)]
#    pivot_idx = lmark
#    while lmark <= rmark:
#        while lmark <= rmark and data[lmark] <= pivot_val:
#            lmark += 1
#        while lmark <= rmark and data[rmark] >= pivot_val:
#            rmark -= 1
#        if lmark <= rmark:
#            swap(data, lmark, rmark)
#            lmark += 1
#            rmark -= 1
#    swap(data, pivot_idx, rmark)
#    return rmark

#def Random(data, lmark, rmark):
#    pivot_val = data[random.randrange(lmark,rmark+1)]
#    pivot_idx = lmark
#    while lmark <= rmark:
#        while lmark <= rmark and data[lmark] <= pivot_val:
#            lmark += 1
#        while lmark <= rmark and data[rmark] >= pivot_val:
#            rmark -= 1
#        if lmark <= rmark:
#            swap(data, lmark, rmark)
#            lmark += 1
#            rmark -= 1
#    swap(data, pivot_idx, rmark)
#    return rmark


#def Last(data, lmark, rmark):
#    pivot_val = data[rmark]
#    pivot_idx = lmark
#    while lmark <= rmark:
#        while lmark <= rmark and data[lmark] <= pivot_val:
#            lmark += 1
#        while lmark <= rmark and data[rmark] >= pivot_val:
#            rmark -= 1
#        if lmark <= rmark:
#            swap(data, lmark, rmark)
#            lmark += 1
#            rmark -= 1
#    swap(data, pivot_idx, rmark)
#    return rmark




#def quickSort(data, pivotMethod):
#    def _qsort(data, first, last):
#        if first < last:
#            splitpoint = pivotMethod(data, first, last)
#            _qsort(data, first, splitpoint-1)
#            _qsort(data, splitpoint+1, last)
#    _qsort(data, 0, len(data)-1)

def lastp(data, p, last):
    x=data[last]
    i=p-1
    j=p
    while j <= (last-1):
        if data[j] <= x:
            i+=1
            swap(data,i,j)
        j+=1
    swap(data,i+1,last)
    return i+1

def randomp(data, p, last):
    x=data[random.randrange(p,last+1)]
    i=p-1
    j=p
    while j <= last-1:
        if data[j] <= x:
            i+=1
            swap(data,i,j)
        j+=1
    swap(data,i+1,last)
    return i+1

def middlep(data, p, last):
    x=data[int((p+last)/2)]
    i=p-1
    j=p
    while j <= last-1:
        if data[j] <= x:
            i+=1
            swap(data,i,j)
        j+=1
    swap(data,i+1,last)
    return i+1

def quickSort(data, first, last,pivot):           # ▷ A[p...r]을 정렬한다 
    if first<last:
        q = pivot(data, first, last)  #▷ 분할 
        quickSort(data, first, q-1,pivot)    #▷ 왼쪽 부분배열 정렬 
        quickSort(data, q+1, last,pivot) #▷ 오른쪽 부분배열 정렬 
    return

def quick_sorted(arr,pivot_temp):
    if pivot_temp is "last":
        pivot_num=len(arr)-1
    elif pivot_temp is "random":
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

BArray1_RV=[]
SArray1_RV=[]
IArray1_RV=[]
MArray1_RV=[]
Q1Array1_RV=[]
Q2Array1_RV=[]
Q3Array1_RV=[]
BArray2_RV=[]
SArray2_RV=[]
IArray2_RV=[]
MArray2_RV=[]
Q1Array2_RV=[]
Q2Array2_RV=[]
Q3Array2_RV=[]
BArray3_RV=[]
SArray3_RV=[]
IArray3_RV=[]
MArray3_RV=[]
Q1Array3_RV=[]
Q2Array3_RV=[]
Q3Array3_RV=[]



Array1_RD=[]
Array2_RD=[]
Array3_RD=[]

for i in range(1000):
    BArray1_RV.append(1000-i)
    SArray1_RV.append(1000-i)
    IArray1_RV.append(1000-i)
    MArray1_RV.append(1000-i)
    Q1Array1_RV.append(1000-i)
    Q2Array1_RV.append(1000-i)
    Q3Array1_RV.append(1000-i)
    Array1_RD.append(random.randrange(1,1001))
for i in range(10000):
    BArray2_RV.append(10000-i)
    SArray2_RV.append(10000-i)
    IArray2_RV.append(10000-i)
    MArray2_RV.append(10000-i)
    Q1Array2_RV.append(10000-i)
    Q2Array2_RV.append(10000-i)
    Q3Array2_RV.append(10000-i)
    Array2_RD.append(random.randrange(1,10001))
for i in range(100000):
    BArray3_RV.append(100000-i)
    SArray3_RV.append(100000-i)
    IArray3_RV.append(100000-i)
    MArray3_RV.append(100000-i)
    Q1Array3_RV.append(100000-i)
    Q2Array3_RV.append(100000-i)
    Q3Array3_RV.append(100000-i)
    Array3_RD.append(random.randrange(1,100001))



BArray1_RD=list(Array1_RD)
SArray1_RD=list(Array1_RD)
IArray1_RD=list(Array1_RD)
MArray1_RD=list(Array1_RD)
Q1Array1_RD=list(Array1_RD)
Q2Array1_RD=list(Array1_RD)
Q3Array1_RD=list(Array1_RD)

BArray2_RD=list(Array2_RD)
SArray2_RD=list(Array2_RD)
IArray2_RD=list(Array2_RD)
MArray2_RD=list(Array2_RD)
Q1Array2_RD=list(Array2_RD)
Q2Array2_RD=list(Array2_RD)
Q3Array2_RD=list(Array2_RD)

BArray3_RD=list(Array3_RD)
SArray3_RD=list(Array3_RD)
IArray3_RD=list(Array3_RD)
MArray3_RD=list(Array3_RD)
Q1Array3_RD=list(Array3_RD)
Q2Array3_RD=list(Array3_RD)
Q3Array3_RD=list(Array3_RD)

def printresult(Method,array):
    start = timeit.default_timer()
    Method(array)
    end=timeit.default_timer()
    sys.stdout.write(str(round(end-start,3)))
    sys.stdout.write("\t\t")

def Qprintresult(Method,array,pivot):
    start = timeit.default_timer()
    first=0
    last=len(array)-1
    Method(array,pivot)
    end=timeit.default_timer()
    sys.stdout.write(str(round(end-start,3)))
    sys.stdout.write("\t\t")
#    return array_temp


#def printresult(Method,pivot,array): # 퀵소트인경우 피봇을 매개변수로 추가해준다.
#    start = timeit.default_timer()
#    Method(array,pivot)
#    end=timeit.default_timer()
#    sys.stdout.write(str(round(end-start,3)))
#    sys.stdout.write("\t\t")



print("\t\tRandom1000\tReverse1000\tRandom10000\tReverse10000\tRandom100000\tReverse100000")
sys.stdout.write("Bubble\t\t")    
#printresult(bubbleSort,BArray1_RD)
#printresult(bubbleSort,BArray1_RV)
#printresult(bubbleSort,BArray2_RD)
#printresult(bubbleSort,BArray2_RV)
print()

sys.stdout.write("Selection\t")
#printresult(selectionSort,SArray1_RD)
#printresult(selectionSort,SArray1_RV)
#printresult(selectionSort,SArray2_RD)
#printresult(selectionSort,SArray2_RV)
#printresult(selectionSort,SArray3_RD)
#printresult(selectionSort,SArray3_RV)
print()


sys.stdout.write("Insertion\t")
#printresult(insertionSort,IArray1_RD)
#printresult(insertionSort,IArray1_RV)
#printresult(insertionSort,IArray2_RD)
#printresult(insertionSort,IArray2_RV)
#printresult(insertionSort,IArray3_RD)
#printresult(insertionSort,IArray3_RV)
print()

sys.stdout.write("Merge\t\t")
#printresult(mergeSort,MArray1_RD)
#printresult(mergeSort,MArray1_RV)
#printresult(mergeSort,MArray2_RD)
#printresult(mergeSort,MArray2_RV)
#printresult(mergeSort,MArray3_RD)
#printresult(mergeSort,MArray3_RV)
print()

sys.stdout.write("Quick1\t\t")
Qprintresult(quick_sorted,Q1Array1_RD,"last")
Qprintresult(quick_sorted,Q1Array1_RV,"last")
Qprintresult(quick_sorted,Q1Array2_RD,"last")
Qprintresult(quick_sorted,Q1Array2_RV,"last")
#printresult(quickSort,QArray1_RD,Last)
#printresult(quickSort,QArray1_RD,Last)
print()

sys.stdout.write("Quick2\t\t")
#Qprintresult(quickSort,Q2Array1_RD,middlep)
#Qprintresult(quickSort,Q2Array1_RV,middlep)
#Qprintresult(quickSort,Q2Array2_RD,middlep)
#Qprintresult(quickSort,Q2Array2_RV,middlep)
#Qprintresult(quickSort,Q2Array3_RD,midldlep)
#Qprintresult(quickSort,Q2Array3_RD,midldlep)
print()

sys.stdout.write("Quick3\t\t")
#Qprintresult(quickSort,Q3Array1_RD,randomp)
#Qprintresult(quickSort,Q3Array1_RV,randomp)
#Qprintresult(quickSort,Q3Array2_RD,randomp)
#Qprintresult(quickSort,Q3Array2_RV,randomp)
#Qprintresult(quickSort,Q3Array3_RD,randomp)
#Qprintresult(quickSort,Q3Array3_RV,randomp)
print()
