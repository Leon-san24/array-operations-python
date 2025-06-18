def median (pList: list) -> int:
    pList.sort()
    if len(pList) % 2 == 0:
        return (pList[int(len(pList)/2)]+pList[int(len(pList)/2-1)])/2
    else:
        return pList[int(len(pList)/2-0.5)]