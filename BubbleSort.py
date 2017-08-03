def bubbleSort(li):
    for item in range(len(li)-1,0,-1):
        for i in range(item):
            if li[i]>li[i+1]:
                li[i],li[i+1]=li[i+1],li[i]

li=[54,26,93,17,77,31,44,55,20]
bubbleSort(li)
print("BubbleSort: ",li)

def shortBubbleSort(li):
    exchange=True
    itempos=len(li)-1
    while itempos>0 and exchange:
        exchange=False
        for i in range(itempos):
            if li[i]>li[i+1]:
                exchange=True
                li[i],li[i+1]=li[i+1],li[i]
        itempos=itempos-1

li=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(li)
print("ShortBubbleSort: ",li)