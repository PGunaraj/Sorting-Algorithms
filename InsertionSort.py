def insertionSort(li):
    for i in range(1,len(li)):
        val=li[i]
        pos=i
        while pos>0 and val<li[pos-1]:
            li[pos]=li[pos-1]
            pos=pos-1
        li[pos]=val

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)


#optimized code
def insertionSort(li):
    for i in range(1,len(li)):
        pos=i
        while pos>0 and li[pos]<li[pos-1]:
            li[pos],li[pos-1]=li[pos-1],li[pos]
            pos=pos-1

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
