def quick_sort(array):
    if len(array) < 2:
        return array
    # choose pivot to first element
    pivot = array[0]
    # i - end of smaller than pivot element, j - end of checked elements. They start at 1 since 0 is pivot
    i, j = 1, 1
    # rearrange elements based on pivot - larger elements go right and smaller elements go left
    # pivot is still at position 0
    while j < len(array):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    # move pivot to its correct place - the i-th element will be the first element larger than pivot
    array[0], array[i - 1] = array[i - 1], array[0]
    # recursively call for left and right parts of array around pivot
    left, right = array[:i - 1], array[i:]
    array[:i - 1] = quick_sort(left)
    array[i:] = quick_sort(right)
    return array


if __name__ == "__main__":
    arr = [12, 45, 2, 34, 2, 3, 18, 8, 9, 5, 3, 4, 15, 17, 15, 18, 3, 44]
    quick_sort(arr)
    print(arr)
