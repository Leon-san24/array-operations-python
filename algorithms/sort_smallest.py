"""
Task number one, find the smallest number of a list with algorithmics and a self build function.

Author: Leon Blyum

"""

def sort_smallest(pList: list) -> int:
    smallest_int = None
    while pList:
        if smallest_int == None or smallest_int > pList[0]:
            smallest_int = pList[0]
        pList.pop(0)
    return smallest_int

