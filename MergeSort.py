def mergeSort(li):
    print("splitting:   ", li)
    if len(li)>1:
        mid=len(li)//2
        left=li[0:mid]
        right=li[mid:len(li)]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                li[k]=left[i]
                i=i+1
            else:
                li[k]=right[j]
                j=j+1
            k=k+1

        while i<len(left):
            li[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            li[k]=right[j]
            j=j+1
            k=k+1

    print("merging: ",li )

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)