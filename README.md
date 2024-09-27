# Bisect_Right_and_Left

### Explanation:

- **`binright(nums, x)`**:
  - It finds the position where `x` should be inserted on the right side in the list `nums` to maintain sorted order.
  - The condition `nums[m] <= x` moves the left pointer `l` rightward, ensuring that the function finds the first element strictly greater than `x`.

- **`binleft(nums, x)`**:
  - It finds the position where `x` should be inserted on the left side in the list `nums` to maintain sorted order.
  - The condition `nums[m] < x` moves the left pointer `l` rightward, ensuring that the function finds the first element greater than or equal to `x`.


    """

    1,2,3,4,4,4,4,5
    
    F,F,F,T,T,T,T,T

    l---------------R

    if We want first T value (first value >= target) as our ans, so retain T,
    if we find T, we know there are 100% more T's in back, but no guarantee in left, so eliminate right T, and make R=M (Retain risky T).

    
    Find the insertion point for x in a sorted list nums to maintain sorted order.
    This function returns the index where x would go, inserting to the left of existing entries.
    Meaning all elements to the left of the index are < x and all elements to the right are >= x.
    """


    """

    1,2,3,4,4,4,4,5

    F,F,F,F,F,F,F,T

    l---------------R

    if We want first T value as our ans, so retain T,
    if we find T, we know there are 100% more T's in back, but no guarantee in left, so eliminate right T, and make R=M (Retain risky T).
    
    Find the insertion point for x in a sorted list nums to maintain sorted order.
    This function returns the index where x would go, inserting to the right of existing entries.
    Meaning all elements to the left of the index are <= x and all elements to the right are > x.
    """
