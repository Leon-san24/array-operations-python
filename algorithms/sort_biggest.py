"""
Task number two, find the biggest number of a list with algorithmics and a self build function.

Author: Leon Blyum

"""

def sort_biggest(pList: list) -> int:
    """ Returns the biggest number as a int from a list.

    Args:
        pList (list): Input list.

    Returns:
        int: Biggest number of the list.
    """
    biggest_int = None
    while pList:
        if biggest_int == None or biggest_int < pList[0]:
            biggest_int = pList[0]
        pList.pop(0)
    return biggest_int
