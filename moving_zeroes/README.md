# Moving Zeroes

Write a function that takes an array of integers and moves each non-zero integer to the left side of the array, then returns the altered array. The order of the non-zero integers does not matter in the mutated array.

1. Understand
  - Restate: take an array and move all the numbers that are not 0 to the left. Move all the 0's toward the end of the array.
  - Inputs and outputs are integers
  - I have enoughinformation to solve this.
2. Examples of this
    - This seems similar to bubble sort or just normal sorting
3. Break it Down
  - traverse over the array
  - if the number is 0, pop it into a temp variable
  - append the variable to the end of the array
  - do that until the end

## Examples
```
Sample input: [0, 3, 1, 0, -2]
Expected output: 3
Expected output array state: [3, 1, -2, 0, 0]
```

```
Sample input: [4, 2, 1, 5]
Expected output: 4
Expected output array state: [4, 2, 1, 5]
```

Can you do this in a single pass through the input array with `O(1)` space?

## Testing
Run the test file by executing `python test_moving_zeroes.py`.

You can also test your implementation manually by executing `python moving_zeroes.py [integers_separated_by_a_single_space]`.


