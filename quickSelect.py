# Selection Function
def QuickSelect(array, left, right, target_index):
    if left == right:  # Target index must be reached.
        return array[left]

    pivot = Partition(array, left, right)
    print(array, pivot, target_index)
    if pivot == target_index:
        return array[target_index]
    elif pivot > target_index:
        return QuickSelect(array, left, pivot - 1, target_index)
    else:
        return QuickSelect(array, pivot + 1, right, target_index)


# Naive partition (simply select right). Could select in different ways, ie random.
def Partition(array, left, right):
    pivot_value = array[
        right
    ]  # Must also move pivot to the right - not a problem for us, pivot is right!

    return_index = left

    for i in range(left, right):
        if array[i] < pivot_value:
            swap(array, i, return_index)
            return_index += 1

    swap(array, right, return_index)
    return return_index


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


# Initialise example values
array = [3, 2, 1, 7, 5, 6, 4]
left = 0
right = len(array) - 1
target_index = 1  # Second Smallest Value

assert QuickSelect(array, left, right, target_index) == 2
