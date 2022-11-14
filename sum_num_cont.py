#!/usr/bin/env python3
# Created By: Jeremiah Omoike
# Date: November 13 2022
# This program asks user for how many numbers they would like to add then calculates and displays the sum of numbers.


def main():

    # initialize your variables
    Loop_counter = 0  # counter initialization
    sum = 0
    answer = ""
    print()
    print(" Welcome to my number adding program.")
    # User input for number of numbers that they want to add
    print()
    Total_num_as_string = input("Please input how many numbers you want to add: ")
    # converts entered number from a string to an int
    # makes sure that user enters a number and not a string
    try:
        Total_number = int(Total_num_as_string)
        if Total_number >= 0:
            # process
            # calculates the sum of the entered numbers using a while loop and continue statements
            while Loop_counter < Total_number:
                print()
                Adding_number_as_string = input(
                    "Input a number you would like to add: "
                )
                # converts numbers that are being added from string to an int
                # makes sure that user enters an int, not a string
                try:
                    Adding_number = int(Adding_number_as_string)
                    if Adding_number < 0:
                        print()
                        print("Negative numbers cannot be added ")
                        # implementation of the continue statement
                        continue
                    print()
                    print("{} added to sum".format(Adding_number))
                    print()
                    sum = Adding_number + sum
                    Loop_counter = Loop_counter + 1
                    answer += str(Adding_number) + "+"
                except Exception:
                    print()
                    print("{} is not an integer".format(Adding_number))
                    print()
                    continue
            if Loop_counter == Total_number:
                print()
                print("{}0 = {}".format(answer, sum))
                print()
                print("The Total sum of all the numbers is {}".format(sum))
                print()
                print("Thank you for using my program!")
        else:
            print("Please enter a whole number")
            print("")
    except Exception:
        print()
        print("This is not a whole number")


if __name__ == "__main__":
    main()
