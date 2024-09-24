# Bisect_Right_and_Left

### Explanation:

- **`binright(nums, x)`**:
  - It finds the position where `x` should be inserted on the right side in the list `nums` to maintain sorted order.
  - The condition `nums[m] <= x` moves the left pointer `l` rightward, ensuring that the function finds the first element strictly greater than `x`.

- **`binleft(nums, x)`**:
  - It finds the position where `x` should be inserted on the left side in the list `nums` to maintain sorted order.
  - The condition `nums[m] < x` moves the left pointer `l` rightward, ensuring that the function finds the first element greater than or equal to `x`.
