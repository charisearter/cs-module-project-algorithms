# Product of All Other Numbers

Write a function that receives an array of integers and returns an array consisting of the product of all numbers in the array _except_ the number at that index.

Understand

- Restate: Multiply all numbers EXCEPT for current index number
- Examples: math
- Break it down:
  -- Traverse thru array
  -- get current index
  -- multiply all numbers except current index
  -- go to next index and do again
  -- possibly remove current index and then multiply ????
  -- then insert it back and next index is removed and so on?
  For example, given

```
[1, 7, 3, 4]
```

your function should return

```
[84, 12, 28, 21]
```

by calculating

```
[7*3*4, 1*3*4, 1*7*4, 1*7*3]
```

In the above example, the final value at index 0 is the product of every number in the input array _except_ the number at index 0.

Can you do this in `O(n)` time with `O(n)` space _without_ using division?

## Testing

Run the test file by executing `python test_product_of_all_other_numbers.py`.
