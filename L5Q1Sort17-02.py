a = 0
arr = []


def sort1(arr, n):
    if (len(arr) == 0 or n > arr[-1]):
        arr.append(n)
        return
    else:
        temp = arr.pop()
        sort1(arr, n)
        arr.append(temp)


def sortstack(arr):
    if len(arr) != 0:

        temp = arr.pop()
        sortstack(arr)
        sort1(arr, temp)


def printStack(arr):
    for i in arr[::-1]:
        print(i, end=" ")
    print()


if __name__ == '__main__':
    arr.append(5)
    arr.append(1)
    arr.append(2)
    arr.append(6)
    arr.append(4)


    print("Stack elements before sorting: ")
    printStack(arr)

    sortstack(arr)
    print("\nStack elements after sorting: ")
    printStack(arr)
