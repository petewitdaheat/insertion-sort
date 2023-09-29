from selectionsortreverse import *

def main():
    # set up the local varuables to store list and last
    data = []
    last = 0

    # prompt the user to input elements for the list
    data = list(map(int, input("Enter 10 numbers separated by a space: ").split()))

    # prompt the user for last
    last = int(input("Enter the index at which the sort will begin: "))

    # display original unsorted list input by user
    for i in data:
        print(i, end=" ")
    
    # call sort method
    sort(data, last)

    print()

    # display sorted list
    for i in data:
        print(i, end=" ")



if __name__ == "__main__":
    main()