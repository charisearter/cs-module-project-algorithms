# Sliding Window Max

Given an array of integers, there is a sliding window of size `k` which is moving from the left side of the array to the right, one element at a time. You can only interact with the `k` numbers in the window. Return an array consisting of the maximum value of each window of elements.

Understand

- Restate: Make a function that returns an array of highest value in the window of elements. The window is set by 'k'. Those are the only number range it can give max value from until it moves to the right. Gives nev value from set in window in a new array.
- Input is integers as well as K that is also an intger setting window size
  -Output is an array with the highest value for each new window as it oves down the line
  -i think i have enough information to solve
- cur_value, temp_value, highest_value for each window before moving

Examples in Life
--video game. If you have a certain amount of money only those will be available to you, whatever youcan't afford is grayed out or in red.
-- video game levels. Depending on your level or World, only certain items or places are available to you until you level up or find a secret that allows you to skip.
Break it Down
-- whatever k# is, that is the window size
-- only those in that window can be evaluated
-- maybe use range of k???
-- while in that range find the highest value
-- compare values and append highest into highNum array
-- do this repeatedly till end of original array
--return the highNum array

## Example

```
Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Expected Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

Can you implement a solution that calculates all of the maximum sliding window values in O(n) time?

## Testing

Run the test file by executing `python test_sliding_window_max.py`.

There is also a larger test file that you can test your code against by running `python test_sliding_window_max_large_input.py`.

> Note: The text files in the `data/` directory are used by the large input tests.
