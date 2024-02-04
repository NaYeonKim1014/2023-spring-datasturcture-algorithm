def merge_sort_inplace(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort_inplace(left_half)
    merge_sort_inplace(right_half)

    merge(arr, left_half, right_half)


def merge(arr, left, right):
    left_index = 0
    right_index = 0
    arr_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            arr[arr_index] = left[left_index]
            left_index += 1
        else:
            arr[arr_index] = right[right_index]
            right_index += 1
        arr_index += 1

    while left_index < len(left):
        arr[arr_index] = left[left_index]
        left_index += 1
        arr_index += 1

    while right_index < len(right):
        arr[arr_index] = right[right_index]
        right_index += 1
        arr_index += 1


# Example usage
keys = [9, 5, 2, 7, 1, 8]
merge_sort_inplace(keys)
print(keys)
