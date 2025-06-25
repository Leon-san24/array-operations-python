"""
Task six coding a quicksort.

Author: Tom Fischer

"""
def quick_sort(pList: list) -> list:
    """ Choose a divider and sorts all bigger numbers to the right and all smaller to the left.

    Args:
        pList (list): List object filled with only numbers.

    Returns:
        List: Sorted List
    """
    return increment(pList, 0, len(pList))

def increment (pList: list, start: int, end: int) -> list:
    if start + 1 == end or start -1 == end or start == end:
        return pList
    o_end = end
    divider = pList[end - 1]
    for i in range (start, end):
        while pList[i]>divider:
            if i >= end:
                break
            pList[i], pList[end-1] = pList[end-1], pList[i]
            end -= 1
        if i >= end:
            break     
    pList = increment(pList,end,o_end)
    if end == o_end:
        end -=1  
    pList = increment(pList,start,end)
    return pList