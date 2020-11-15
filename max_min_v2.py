def max_min(lst):
    # Return empty list for empty list
    if (len(lst) == 0):
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    print("Starting with {}".format(lst))

    for i in range(len(lst)):
        print("i={} lst={}".format(i,lst))
        # even number means max element to append
        if i % 2 == 0:
            print("i={} maxIdx={} lst[maxIdx]={}".format(i,maxIdx,lst[maxIdx]))
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            print("i={} minIdx={} lst[minIdx]={}".format(i,minIdx,lst[minIdx]))
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1
    print("-"*20)
    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
        print(lst)
    return lst


print(max_min([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
