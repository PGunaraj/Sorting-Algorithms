def quickSort(li):
    quickSortMethod(li, 0, len(li)-1)

def quickSortMethod(li,start,end):
    if start<end:
        split = partition(li, start, end)
        quickSortMethod(li, start, split - 1)
        quickSortMethod(li, split + 1, end)


def partition(li,start,end):
    pivot=li[start]
    left=start+1
    right=end
    done=False

    while not done:
        while left<=right and li[left]<=pivot:
            left=left+1
        while right>=left and li[right]>=pivot:
            right=right-1

        if right<left:
            done=True
        else:
            temp=li[left]
            li[left]=li[right]
            li[right]=temp

    temp=li[start]
    li[start]=li[right]
    li[right]=temp

    return right

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)

