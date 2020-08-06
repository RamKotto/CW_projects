array = [14, 12, 11, 2, 3, 1, 9, 43, 1, 2, 43, 100]


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        support = array[0]
        lower = [i for i in array[1:] if i <= array[0]]
        higher = [i for i in array[1:] if i > array[0]]
        return quick_sort(lower) + [support] + quick_sort(higher)


print(quick_sort(array))


def count(array):
    if array == []:
        return 0
    return 1 + count(array[1:])


print(count(array))


def sum(array):
    if array == []:
        return 0
    return array[0] + sum(array[1:])


print(sum(array))
