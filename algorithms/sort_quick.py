
def quicksort(pList: list) -> list:
    return increment(pList, 0, len(pList))

def increment (pList, start, end):
    if start + 1 == end or start -1 == end or start == end:
        return pList
    oend = end
    divider = pList[end - 1]
    for i in range (start, end):
        while pList[i]>divider:
            if i >= end:
                break
            pList[i], pList[end-1] = pList[end-1], pList[i]
            end -= 1
        if i >= end:
            break     
    pList = increment(pList,end,oend)
    if end == oend:
        end -=1  
    pList = increment(pList,start,end)
    return pList


list = [5,2,8,2,67,2,46,23,56,76,1,43,10]
#list = [6,1,43,10]
print (quicksort(list))
