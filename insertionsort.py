def sort(data, first: int):
    """sorts a list of integers from the smallest to largest
    bypassing the elements to the left of first.

    Args:
        data (int): list of integers
        first (int): the list index at which the sort will begin
    """    
    # initialize loop counter variable i to 1
    i = 1

    #initialize loop counter variable j to 0
    j = 0

    # initialize next value to 0
    nextVal = 0

    # loop through list as many times as speciified by the 
    # length of the list and first
    # this loop represents the blue arrow in the slides
    while(i < len(data) - first):
        # store a copy of a number in index position first + i 
        # in next value
        nextVal = data[first+i]

        # loop through the list starting at the same index as
        # next value and iterate back toward first as long as 
        # the element to the left of next value is greater than
        # next value and we're not the whole way back to first
        j = first + i
        while(j > first and data[j-1] > nextVal):
            # shift the element to the left of the next value right
            # ward one position
            data[j] = data[j - 1]

            # insert next value into the element that was just
            # shifted
            data[j-1] = nextVal

            # decrement j by 1
            j = j-1

        # increment i by 1
        i = i + 1