def selectionSort(li):
    for item in range(len(li)-1,0,-1):
        max=0
        for i in range(1,item+1):
            if li[i]>li[max]:
                max=i
        temp=li[item]
        li[item]=li[max]
        li[max]=temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)