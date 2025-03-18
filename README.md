# Search & Sort Algorithm Implementation (Diabetes Dataset)

## Description
This project implements various searching and sorting algorithms using a real-world diabetes dataset. The implementation includes both searching algorithms (Linear and Binary Search) and sorting algorithms (Bubble Sort, Selection Sort, Insertion Sort, and Quick Sort).

## Features
- Load and process diabetes dataset
- Search functionality:
  - Linear Search
  - Binary Search
- Sorting functionality:
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  - Quick Sort
- Performance measurement for each algorithm
- Save sorted results to CSV file

## Installation
1. Clone this repository:
```bash
git clone https://github.com/yourusername/search-sort-diabetes.git
cd search-sort-diabetes
```

2. Install required libraries:
```bash
pip install pandas
```

## Usage
1. Ensure `diabetes.csv` is in the same directory as the script
2. Run the script:
```bash
python search_sort.py
```

3. Follow the interactive prompts to:
   - Choose a column to search
   - Enter a value to search for
   - Select a search method
   - Choose a column to sort
   - Select a sorting algorithm

## Sample Output
```
Choose a column to search (Glucose, Age, BMI, etc.): Age
Enter a value to search for: 30
Choose search method:
1. Linear Search
2. Binary Search
Enter choice: 2
Sorting "Age" column before Binary Search...
Binary Search: Found at row index 5
Time taken: 0.0001s

Choose a column to sort (Glucose, Age, BMI, etc.): BMI
Choose sorting algorithm:
1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Quick Sort
Enter choice: 4
Sorting by "BMI" using Quick Sort...
Sorting completed.
Sorted data saved as "sorted-diabetes.csv".
Time taken: 0.00005s
```

## Files
- `search_sort.py`: Main Python script containing all implementations
- `diabetes.csv`: Input dataset
- `sorted-diabetes.csv`: Output sorted dataset
