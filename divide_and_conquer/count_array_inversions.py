# The goal here is to count array inversions
# Inversion means an element at a smaller index is bigger than an element at a higher index
# Example: [4,3,2] - here we have 3 inversions - 4 is bigger than 3 and 2 but is at lower index, also 3 > 2 at lower index

def count_inversions(array):
    # first let's make use of divide and conquer - divide into 2 arrays and count inversions in them
    if len(array) < 2:
        return 0
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    # this will count left and right inversions and also sort left and right halves
    inversions = count_inversions(left) + count_inversions(right)
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
            inversions += (len(left) - i)
            # inversion only exists if an element of the right sorted array is smaller than element of left sorted array
            # the inversions correspond to the number of elements left in left array after the corresponding right element is moved
        k += 1

    # here we can have leftover elements that are not taken care of e.g. if the array has odd num elements
    # this matters because the array has to be merged properly over each recursive call, otherwise elements are lost

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return inversions


if __name__ == "__main__":
    print(count_inversions([1, 3, 5, 2, 4, 0]))
