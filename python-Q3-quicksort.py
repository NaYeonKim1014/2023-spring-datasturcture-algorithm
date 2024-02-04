def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    smaller = []
    equal = []
    larger = []

    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)

    return quicksort(smaller) + equal + quicksort(larger)


# Example usage
keys = [9, 5, 2, 7, 1, 8]
sorted_keys = quicksort(keys)
print(sorted_keys)
