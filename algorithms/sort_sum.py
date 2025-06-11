
def sort_sum (pList: list) -> int:
    sum = 0
    for i in pList:
        sum += i
    return sum

def sort_average (pList: list) -> int:
    sum = sort_sum(pList)
    return sum/len(pList)




List = [4,2,8,4,9,2,45,23,8,1]
print(sort_sum(List))
print(sort_average(List))
