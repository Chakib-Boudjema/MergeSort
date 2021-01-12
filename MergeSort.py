def MergeSort(Array):
    if(len(Array)<2):
        return
    mid=len(Array)//2
    LeftArray=Array[:mid]
    RightArray=Array[mid:]
    MergeSort(LeftArray)
    MergeSort(RightArray)
    i=0
    j=0
    k=0
    while i<len(LeftArray) and j<len(RightArray):
        if(LeftArray[i]<=RightArray[j]):
            Array[k]=LeftArray[i]
            i+=1
        else:
            Array[k]=RightArray[j]
            j+=1
        k+=1
    if(j<len(RightArray)):
        Array[k:]=RightArray[j:]
    else:
        Array[k:]=LeftArray[i:]
#test
arr=[15,24,36,51,-10,5,9,100,101,14,25,78]
print(arr)
MergeSort(arr)
print(arr)