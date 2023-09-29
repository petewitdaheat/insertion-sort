def sort(data, last: int):
    """ Sorts a list of integers from smallest to largest
    bypassing the elements to the left of the last.

    Args:
        data (int): list of integers
        last (int): the list index at which the sort will begin.
    """   
    # initialize loop counter variable named i
    i = len(data) + last + 1

    # initialize loop counter variable named j to 0
    j = 0

    # initialize variable named small that will be used to store
    # index of the biggest value
    small = 0

    # initialize variable named temp that will be used
    # to swap list values
    temp = 0

    # loop through list as many times as specified by
    # len(data) and last
    # this loop represents the blue arrow
    while (i > 0):
        # set small equal to last
        small = last

        # set j equal to last - 1
        j = last - 1

        # loop through the list starting with the element at 
        # last - 1 and continue until reach last - i
        # this loop represents the yellow arrow
        while (j >= last - i):
            # if the value in data[small] is less than 
            # data[j]
            if(data[small] < data[j]):
                # set small equal to j
                small = j
            # decrement j by 1
            j -= 1
        
        # swap the data in last + i with the data in small
        # set temp to value in data[last + i]
        temp = data[last - i]

        # set data[last + i] to the value in data[small]
        data[last - i] = data[small]

        # set data[small] to the value in temp
        data[small] = temp

        # increment i by 1
        i -= 1

