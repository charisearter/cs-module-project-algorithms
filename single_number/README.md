# Single Number

Given a non-empty array of integers where every element appears twice except for one. Find that single number. You may assume that there will _always_ be _one_ odd-number-out and every other number in the input shows up exactly twice.  

My notes:

Understanding Problem:
Restate the problem: Find the number that only appears one time in an array.
Inputs: THe array is integers. Possibly could have floats
Output: Should spit out the single integer or float
Labeling: I could name the single numbeer solo

Explore Concrete Examples:
This reminds me of the counting sort algorithm mixed with the find the target number iteration algorithm.  But the output spits out the number(s) that only appear once.

Break it Down:
set up a empty dictionary to count
Traverse of the array
Any number not present in the dictionary should be added and set it's value to 1.
If it is already in there it should add +1 each time occurs
then the count dicitonary should be traversed
It should give the key that has the value of 1.
return the number

## Examples
```
Sample input: [2, 2, 1]
Expected output: 1
```

```
Sample iput: [4, 1, 2, 1, 2]
Expected output: 4
```

Can you implement a solution that finds the single number in _one_ pass through the input array with `O(1)` space complexity?

## Testing
Run the test file by executing `python test_single_number.py`. 
