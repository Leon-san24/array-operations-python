"""
Task number five, build a function to find the median using the built in sort function.

Author: Tom Fischer

"""
def sort_median (pList: list) -> int:
    """ Returns the median number of a list as a float.

    Args:
        pList (list): Input list.

    Returns:
        float: Median number of the list.
    """
    pList.sort()
    if len(pList) % 2 == 0:
        return float((pList[int(len(pList)/2)]+pList[int(len(pList)/2-1)])/2)
    else:
        return float(pList[int(len(pList)/2-0.5)])