'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # traverse the array
    # if number is not 0 move to the front of list /or just go to next number
    # if number is 0 move to the end of list / or pop it from array into temp variable and the append it to array at the end
    zeros = []
    others = []
    for num in arr:
        if num == 0:
            zeros.append(num)
        else:
            others.append(num)
    others.extend(zeros)
    return others  # return array


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
