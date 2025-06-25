"""
Task three and four, add all elements of a list together and find the average.

Author: Tom Fischer

"""


def list_sum (pList: list) -> float:
    """ Adds all elements of a list together into a integer.

    Args:
        pList (list): List object filled with only numbers.

    Returns:
        float: Value of all elements of the list combined.
    """
    sum = 0
    for i in pList:
        sum += i
    return sum


def list_average (pList: list) -> float:
    """Returns the avarage value of a given list.

    Args:
        pList (list): List object with only numbers.

    Returns:
        float: Avarage Value
    """
    sum = list_sum(pList)
    return sum/len(pList)


test_list = [4,2,8,4,9,2,45,23,8,1]
print(list_sum(test_list))
print(list_average(test_list))
