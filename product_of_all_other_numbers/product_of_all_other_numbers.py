

'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):

    #   -- Traverse thru array
    # -- get current index
    # -- multiply all numbers except current index
    # -- store results in a new array -- going forward
    # -- reverse original array and multiply all numbers except current index
    # store in a different array
    # make final array
    # multiply the other 2 arrays together and appen it to final
    # return final  --> linear O(n)

    left = [1] * len(arr)  # multiply all numbers forwards
    right = [1] * len(arr)  # mulitply all numbers going backwards
    final = []  # mulitply left and right with each other

    for i in range(1, len(arr)):  # range will go thru length of array, starting at 1
        left[i] = (left[i - 1] * arr[i-1])
    for j in range(len(arr) - 2, -1, -1):  # start at end, countdown to 0, decrement by 1

        right[j] = (right[j+1] * arr[j+1])
    print('left: ', left)
    print('right: ', right)
    for k in range(len(left)):
        final.append(left[k] * right[k])
    return final


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
