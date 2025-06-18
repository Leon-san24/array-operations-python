"""
Task number six, develop a sort algorythm.

Author: Leon Blyum

"""



def bubble_sort(pList: list) -> list:
    """ A simple implementation of the bubblesort alogrythm for sorting lists.

    Args:
        pList (list): List of numbers with unsorted objects.

    Returns:
        list: List of sorted numbers.
    """

    for i in range(len(pList)):
        for j in range(len(pList)-i-1):
            if pList[j] > pList[j+1]:
                pList[j], pList[j + 1] = pList[j + 1], pList[j]
    
    return pList

def merge(pLeft: list, pRight: list) -> list:
    """ Helper function of merge_sort, it merges to list parts together in the correct order.

    Args:
        pLeft (list): Left list part.
        pRight (list): Right list part.

    Returns:
        list: Returns a fully sorted merged list.
    """
    sorted_list = []
    i = j = 0
    while i < len(pLeft) and j < len(pRight):
        if pLeft[i] < pRight[j]:
            sorted_list.append(pLeft[i])
            i += 1
        else:
            sorted_list.append(pRight[j])
            j += 1
    sorted_list.extend(pLeft[i:])
    sorted_list.extend(pRight[j:])
    return sorted_list

def merge_sort(pList: list) -> list:
    """ The main sort function, it recursivly splits the the given list until it isnt possible anymore and the calls merge to set
    them together.

    Args:
        pList (list): Unsorted list of numbers.

    Returns:
        list: Sorted list of numbers.
    """
    if len(pList) <= 1:
        return pList
    mid = len(pList) // 2
    left = merge_sort(pList[:mid])
    right = merge_sort(pList[mid:])
    return merge(left, right)


    

def insertion_sort():
    NotImplemented