def binright(nums, x):
    """
    Find the insertion point for x in a sorted list nums to maintain sorted order.
    This function returns the index where x would go, inserting to the right of existing entries.
    Meaning all elements to the left of the index are <= x and all elements to the right are > x.
    """
    l = 0
    r = len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] <= x:
            l = m + 1  # Move right if nums[m] is less than or equal to x
        else:
            r = m  # Keep the current position, move left
    return l

def binleft(nums, x):
    """
    Find the insertion point for x in a sorted list nums to maintain sorted order.
    This function returns the index where x would go, inserting to the left of existing entries.
    Meaning all elements to the left of the index are < x and all elements to the right are >= x.
    """
    l = 0
    r = len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] < x:
            l = m + 1  # Move right if nums[m] is less than x
        else:
            r = m  # Keep the current position, move left
    return l

# Examples to demonstrate the usage of binright and binleft

# A sorted list of numbers
nums = [1, 2, 4, 4, 4, 5, 7, 9]

# Example for binright
print("Using binright:")
print("Index to insert 4 (to the right):", binright(nums, 4))  # Output should be 5
print("Index to insert 6 (to the right):", binright(nums, 6))  # Output should be 6

# Example for binleft
print("\nUsing binleft:")
print("Index to insert 4 (to the left):", binleft(nums, 4))    # Output should be 2
print("Index to insert 6 (to the left):", binleft(nums, 6))    # Output should be 6

# Explanation:
# In binright, we look for the position where elements are strictly greater than x.
# In binleft, we look for the position where elements are greater than or equal to x.
