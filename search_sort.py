import pandas as pd
import time

# Load the dataset
def load_dataset(filename):
    """Load the diabetes dataset from CSV file"""
    return pd.read_csv(filename)

# Search Algorithms
def linear_search(theValues, target):
    """Perform linear search on an unsorted array"""
    start_time = time.time()
    n = len(theValues)
    for x in range(n):
        if theValues[x] == target:
            return x, time.time() - start_time
    return -1, time.time() - start_time

def sorted_linear_search(theValues, target):
    """Perform linear search on a sorted array"""
    start_time = time.time()
    n = len(theValues)
    for x in range(n):
        if theValues[x] == target:
            return x, time.time() - start_time
        elif theValues[x] > target:
            return -1, time.time() - start_time
    return -1, time.time() - start_time

def binary_search(theValues, target):
    """Perform binary search on a sorted array"""
    start_time = time.time()
    low = 0
    high = len(theValues) - 1
    while low <= high:
        mid = (high + low) // 2
        if theValues[mid] == target:
            return mid, time.time() - start_time
        elif target < theValues[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1, time.time() - start_time

# Sorting Algorithms
def bubble_sort(arr):
    """Perform bubble sort on an array"""
    start_time = time.time()
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, time.time() - start_time

def selection_sort(arr):
    """Perform selection sort on an array"""
    start_time = time.time()
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr, time.time() - start_time

def insertion_sort(arr):
    """Perform insertion sort on an array"""
    start_time = time.time()
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr, time.time() - start_time

def quick_sort(arr):
    """Perform quick sort on an array"""
    start_time = time.time()
    arr = arr.copy()
   
    if len(arr) <= 1:
        return arr, time.time() - start_time
       
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
   
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        elif x > pivot:
            right.append(x)
           
    sorted_left, _ = quick_sort(left)
    sorted_right, _ = quick_sort(right)
    result = sorted_left + middle + sorted_right
    return result, time.time() - start_time

def main():
    # Load dataset
    df = load_dataset('diabetes.csv')
   
    # Search functionality
    print("Choose a column to search (Glucose, Age, BMI, etc.):", end=" ")
    search_column = input().strip()
   
    if search_column not in df.columns:
        print(f"Error: Column '{search_column}' not found in dataset")
        return
       
    print("Enter a value to search for:", end=" ")
    try:
        search_value = float(input().strip())
    except ValueError:
        print("Error: Please enter a numeric value")
        return
       
    print("Choose search method:")
    print("1. Linear Search")
    print("2. Binary Search")
    print("Enter choice:", end=" ")
    search_choice = input().strip()
   
    column_values = df[search_column].values.tolist()
   
    if search_choice == "1":
        index, time_taken = linear_search(column_values, search_value)
        method = "Linear Search"
    elif search_choice == "2":
        sorted_values = sorted(column_values)
        index, time_taken = binary_search(sorted_values, search_value)
        method = "Binary Search"
    else:
        print("Invalid search choice")
        return
       
    if index != -1:
        if search_choice == "2":
            original_index = column_values.index(sorted_values[index])
            print(f"{method}: Found at row index {original_index}")
        else:
            print(f"{method}: Found at row index {index}")
    else:
        print(f"{method}: Value not found")
    print(f"Time taken: {time_taken:.6f}s")
       
    # Sorting functionality
    print("\nChoose a column to sort (Glucose, Age, BMI, etc.):", end=" ")
    sort_column = input().strip()
   
    if sort_column not in df.columns:
        print(f"Error: Column '{sort_column}' not found in dataset")
        return
       
    print("Choose sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Quick Sort")
    print("Enter choice:", end=" ")
    sort_choice = input().strip()
   
    column_values = df[sort_column].values.tolist()
   
    if sort_choice == "1":
        print(f'Sorting by "{sort_column}" using Bubble Sort...')
        sorted_values, time_taken = bubble_sort(column_values)
    elif sort_choice == "2":
        print(f'Sorting by "{sort_column}" using Selection Sort...')
        sorted_values, time_taken = selection_sort(column_values)
    elif sort_choice == "3":
        print(f'Sorting by "{sort_column}" using Insertion Sort...')
        sorted_values, time_taken = insertion_sort(column_values)
    elif sort_choice == "4":
        print(f'Sorting by "{sort_column}" using Quick Sort...')
        sorted_values, time_taken = quick_sort(column_values)
    else:
        print("Invalid sorting choice")
        return
       
    # Create sorted DataFrame and save to CSV
    sorted_indices = [column_values.index(x) for x in sorted_values if x in column_values]
    sorted_df = df.iloc[sorted_indices].reset_index(drop=True)
    sorted_df.to_csv('test_sorted-diabetes.csv', index=False)
   
    print("Sorting completed.")
    print('Sorted data saved as "sorted-diabetes.csv".')
    print(f"Time taken: {time_taken:.6f}s")

if __name__ == "__main__":
    main()