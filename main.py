"""
The main launch file for all examples of the arrays operations.

Authors: Leon Blyum, Tom Fischer, Luca Pydde
"""

import sys
import ast
import time
import os
from algorithms.sort_biggest import sort_biggest
from algorithms.sort_smallest import sort_smallest
from algorithms.list_sum import list_sum, list_average
from algorithms.sort_median import sort_median
from algorithms.sort_list import bubble_sort, merge_sort


def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def parse_list_input(input_str: str) -> list:
    """Parse string input to list, handling various formats.

    Args:
        input_str (str): A string of numbers diivided by ,

    Raises:
        ValueError: Non int object in the list
        ValueError: Invalid format

    Returns:
        list: Returns a python list
    """
    try:
        if input_str.strip().startswith('[') and input_str.strip().endswith(']'):
            parsed = ast.literal_eval(input_str.strip())
        else:
            parsed = [float(x.strip()) for x in input_str.split(',')]
            parsed = [int(x) if x.is_integer() else x for x in parsed]
        
        if not all(isinstance(x, (int, float)) for x in parsed):
            raise ValueError("All elements must be numbers")
        
        return parsed
    except (ValueError, SyntaxError):
        raise ValueError(f"Invalid list format: {input_str}")


def get_list_input() -> list:
    """Get list input from user.

    Returns:
        list: returns python list from user input
    """
    while True:
        try:
            print("Enter your list (e.g., [1,2,3] or 1,2,3):")
            user_input = input("List: ").strip()
            if user_input:
                return parse_list_input(user_input)
            print("Please enter a valid list.")
        except ValueError as e:
            print(f"Error: {e}")


def time_function(func, *args):
    """Time a function execution and return result with timing info.

    Args:
        func (_type_): The functions that gets timed

    Returns:
        _type_: returns the output of the function and a execution time.
    """
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return result, execution_time


def main():
    """Main programm runner.
    """
    default_list = [4, 23, 8, 13, 7, 9, 42, 11, 6, 80, 3]
    
    # Handle command line arguments
    if len(sys.argv) > 1:
        try:
            if len(sys.argv) == 2:
                numbers = parse_list_input(sys.argv[1])
            else:
                numbers = [float(x) for x in sys.argv[1:]]
                numbers = [int(x) if x == int(x) else x for x in numbers]
            print(f"Using command line list: {numbers}")
        except ValueError:
            print("Error parsing arguments. Using default list.")
            numbers = default_list
    else:
        print("Python List Operations")
        print(f"Default list: {default_list}")
        use_default = input("Use default list? (y/n): ").strip().lower()
        numbers = default_list if use_default in ['y', 'yes', ''] else get_list_input()
    
    # Main loop
    while True:
        try:
            clear_terminal()
            print(f"Working with list: {numbers}")
            print("\nChoose a task:")
            print("1. Find smallest number")
            print("2. Find largest number") 
            print("3. Calculate sum")
            print("4. Calculate average")
            print("5. Find median")
            print("6. Sort list")
            print("0. Exit")
            
            choice = input("Choice (0-6): ").strip()
            clear_terminal()
            
            match choice:
                case '0':
                    break
                case '1':
                    result, exec_time = time_function(sort_smallest, numbers.copy())
                    print(f"List: {numbers}")
                    print(f"Smallest: {result}")
                    print(f"Execution time: {exec_time:.4f} ms")
                case '2':
                    result, exec_time = time_function(sort_biggest, numbers.copy())
                    print(f"List: {numbers}")
                    print(f"Largest: {result}")
                    print(f"Execution time: {exec_time:.4f} ms")
                case '3':
                    result, exec_time = time_function(list_sum, numbers)
                    print(f"List: {numbers}")
                    print(f"Sum: {result}")
                    print(f"Execution time: {exec_time:.4f} ms")
                case '4':
                    result, exec_time = time_function(list_average, numbers)
                    print(f"List: {numbers}")
                    print(f"Average: {result:.2f}")
                    print(f"Execution time: {exec_time:.4f} ms")
                case '5':
                    result, exec_time = time_function(sort_median, numbers.copy())
                    print(f"List: {numbers}")
                    print(f"Median: {result}")
                    print(f"Execution time: {exec_time:.4f} ms")
                case '6':
                    print(f"List: {numbers}")
                    print("1. Bubble Sort")
                    print("2. Merge Sort")
                    sort_choice = input("Sort choice (1-2): ").strip()
                    clear_terminal()
                    match sort_choice:
                        case '1':
                            result, exec_time = time_function(bubble_sort, numbers.copy())
                            print(f"Original: {numbers}")
                            print(f"Bubble Sort: {result}")
                            print(f"Execution time: {exec_time:.4f} ms")
                        case '2':
                            result, exec_time = time_function(merge_sort, numbers.copy())
                            print(f"Original: {numbers}")
                            print(f"Merge Sort: {result}")
                            print(f"Execution time: {exec_time:.4f} ms")
                        case _:
                            print("Invalid sort choice.")
                case _:
                    print("Invalid choice.")
            
            if choice != '0':
                input("\nPress Enter to continue...")
                    
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()