def linear_search(table, x):
    """Linear search for hash table.

    Args:
        table: List[List[Tuple[int, Any]]], where each list is a bucket of (key, value) pairs.
        x: The key to search for.

    Returns:
        The bucket address of x if x is in the table, -1 otherwise.
    """
    for bucket in table:
        for key, value in bucket:
            if key == x:
                return bucket
    return -1


# Example usage
hash_table = [[] for _ in range(10)]  # Initialize hash table with 10 empty buckets
hash_table[0].append((1, 'one'))
hash_table[0].append((2, 'two'))
hash_table[1].append((3, 'three'))

# Search for key 2
result = linear_search(hash_table, 2)
if result == -1:
    print("Key not found")
else:
    print(f"Key found in bucket {result}")

# Search for key 4
result = linear_search(hash_table, 4)
if result == -1:
    print("Key not found")
else:
    print(f"Key found in bucket {result}")
