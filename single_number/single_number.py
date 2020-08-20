'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # if no method already built in
    # make empty dictionary to store each element in the array
    # traverse the array
    # if the dictionary does not have the element - add it and set to 1
    # if element is present add +1 each time that element appears
    # traverse the dictionary (maybe if statment)
    # check for the element that has the value of 1
    # return that element
    #-----------------------------
    # if built in figure out how to manipulate the method to only return the number that appears once
    for num in arr:
        if arr.count(num) == 1:
            return num


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
