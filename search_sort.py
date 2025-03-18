import pandas as pd
import time

# Load the dataset
def load_dataset(filename):
    """Load the diabetes dataset from CSV file"""
    return pd.read_csv(filename)

# Search Algorithms
def linear_search(arr, target):
    """
    Perform linear search on an array
    Returns: (index if found or -1 if not found, time taken)
    """
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == target:
            end_time = time.time()
            return i, end_time - start_time
    end_time = time.time()
    return -1, end_time - start_time

def binary_search(arr, target):
    """
    Perform binary search on a sorted array
    Returns: (index if found or -1 if not found, time taken)
    """
    start_time = time.time()
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            end_time = time.time()
            return mid, end_time - start_time
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    end_time = time.time()
    return -1, end_time - start_time

# Sorting Algorithms
def bubble_sort(arr):
    """
    Perform bubble sort on an array
    Returns: (sorted array, time taken)
    """
    start_time = time.time()
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    end_time = time.time()
    return arr, end_time - start_time

def selection_sort(arr):
    """
    Perform selection sort on an array
    Returns: (sorted array, time taken)
    """
    start_time = time.time()
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    end_time = time.time()
    return arr, end_time - start_time

def insertion_sort(arr):
    """
    Perform insertion sort on an array
    Returns: (sorted array, time taken)
    """
    start_time = time.time()
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
    end_time = time.time()
    return arr, end_time - start_time

def quick_sort_partition(arr, low, high):
    """Helper function for quick sort - performs partitioning"""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_helper(arr, low, high):
    """Helper function for quick sort - recursive implementation"""
    if low < high:
        pi = quick_sort_partition(arr, low, high)
        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)

def quick_sort(arr):
    """
    Perform quick sort on an array
    Returns: (sorted array, time taken)
    """
    start_time = time.time()
    arr = arr.copy()
    quick_sort_helper(arr, 0, len(arr) - 1)
    end_time = time.time()
    return arr, end_time - start_time

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
        if index != -1:
            print(f"Linear Search: Found at row index {index}")
        else:
            print("Linear Search: Value not found")
        print(f"Time taken: {time_taken:.6f}s")
        
    elif search_choice == "2":
        print(f'Sorting "{search_column}" column before Binary Search...')
        sorted_values = sorted(column_values)
        sorted_indices = [column_values.index(x) for x in sorted_values]
        
        index, time_taken = binary_search(sorted_values, search_value)
        if index != -1:
            original_index = sorted_indices[index]
            print(f"Binary Search: Found at row index {original_index}")
        else:
            print("Binary Search: Value not found")
        print(f"Time taken: {time_taken:.6f}s")
        
    else:
        print("Invalid search choice")
        return
        
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
    sorted_indices = [column_values.index(x) for x in sorted_values]
    sorted_df = df.iloc[sorted_indices].reset_index(drop=True)
    sorted_df.to_csv('sorted-diabetes.csv', index=False)
    
    print("Sorting completed.")
    print('Sorted data saved as "sorted-diabetes.csv".')
    print(f"Time taken: {time_taken:.6f}s")

if __name__ == "__main__":
    main()
