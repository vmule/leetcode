# Binary search


def recursiveBinarySearch(alist, low, high, target):
    if high >= low and high < len(alist) - 1:
        mid = (low + high) // 2

        if alist[mid] == target:
            return mid

        elif target < alist[mid]:
            return recursiveBinarySearch(alist, low, mid - 1, target)

        elif target > alist[mid]:
            return recursiveBinarySearch(alist, mid, high + 1, target)

    else:
        return -1


def iterativeBinarySearch(alist, target):
    low = 0
    high = len(alist) - 1

    while low <= high:
        mid = (low + high) // 2

        if alist[mid] == target:
            return mid

        if alist[mid] > target:
            high = mid - 1

        elif alist[mid] < target:
            low = mid + 1

    return -1


alist = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# alist = [2, 3, 4, 10, 40]
target = 1

result = recursiveBinarySearch(alist, 0, len(alist) - 1, target)
result2 = iterativeBinarySearch(alist, target)

if result >= 0:
    print(
        "Target: {0} found using recursiveBinarySearch at index: {1}.".format(
            target, result
        )
    )
else:
    print("Target: {0} not found, using recursiveBinarySearch.".format(target))

if result2 >= 0:
    print(
        "Target: {0} found using iterativeBinarySearch at index: {1}.".format(
            target, result
        )
    )
else:
    print("Target: {0} not found, using recursiveBinarySearch.".format(target))
