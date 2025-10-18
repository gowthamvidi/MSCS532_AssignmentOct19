# Quicksort Algorithm – Deterministic vs Randomized

## Overview
This project implements and compares two versions of the **Quicksort** algorithm:

1. **Deterministic Quicksort** – always selects the **last element** as the pivot.  
2. **Randomized Quicksort** – selects a **random pivot** from the subarray to reduce the chance of encountering the worst case.

Both algorithms are tested with various input distributions to observe performance differences and understand how pivot selection impacts efficiency.

---

## How to Run

### **Requirements**
- Python 3.8 or higher  
- No external dependencies (uses only built-in libraries `random` and `time`)

### **Steps**
1. Clone or download this repository.  
2. Save the script as `quicksort.py` (if not already).  
3. Open a terminal in the project folder and run:

   python quicksort.py


### **Summary of Findings**


Distribution             Algorithm             Time        First 10 Elements
-----------------------------------------------------------------------------
Random (n=10)            quicksort             0.000024s   [1, 2, 3, 5, 7, 8, 9, 10]  
Random (n=10)            randomized_quicksort  0.000018s   [1, 2, 3, 5, 7, 8, 9, 10]  
Sorted (n=10)            quicksort             0.000036s   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
Reverse-sorted (n=10)    randomized_quicksort  0.000022s   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  

The output will show execution time and sorted results for different types of input data.  

The results demonstrate how pivot selection directly influences the efficiency of Quicksort.  
While the deterministic approach is simple, it is highly sensitive to input order.  
The randomized version consistently outperforms it by avoiding repetitive worst-case splits, making it the practical choice for large-scale and unpredictable data in modern computing.