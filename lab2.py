# FUNCTION TO ADD NUMBERS UNTIL TARGET IS REACHED


def sum_to_goal(numbers, target):
    total = 0
    for number in numbers:
        total += number
        if total >= target:
            break
    return total

# LAB 2 - ONLY REQUIRED FUNCTIONS COPIED FROM LAB 1


# FOLLOWING FUNCTIONS WERE USED FOR TIMING AND ANALYSIS



# FUNCTION: Fibonacci() FROM LAB 1

# FUNCTION TO COMPUTE FIBONACCI NUMBER RECURSIVELY


def Fibonacci(index_position):
    if index_position == 0:
        return 0
    elif index_position == 1:
        return 1
    previous_number, current_number = 0, 1
    for counter in range(2, index_position + 1):
        previous_number, current_number = current_number, previous_number + current_number
    return current_number

# FUNCTION: sum_to_goal() FROM LAB 1

# TEST CALLS TO DISPLAY OUTPUT DURING GITHUB ACTIONS

# MAIN PROGRAM ENTRY POINT TO RUN TESTS




if __name__ == "__main__":
    import time  # IMPORT MODULE TO TRACK EXECUTION TIME

    # MEASURE TIME FOR sum_to_goal FUNCTION


    start = time.time()
    print(f"sum_to_goal([100, 200, 300], 400) = {sum_to_goal([100, 200, 300], 400)}")
    print(f"TIME TAKEN: {time.time() - start:.6f} SECONDS")

    # MEASURE TIME FOR Fibonacci FUNCTION


    start = time.time()
    print(f"Fibonacci(10) = {Fibonacci(10)}")
    print(f"TIME TAKEN: {time.time() - start:.6f} SECONDS")