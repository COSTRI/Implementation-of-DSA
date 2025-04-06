# Implementation of Sorting Algorithms

# Bubble Sort
def bubble_sort(arr):
    """
    Bubble Sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. This process is repeated
    until the list is sorted.
    """
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Outer loop for each pass
        for j in range(0, n-i-1):  # Inner loop for comparing adjacent elements
            if arr[j] > arr[j+1]:  # If the current element is greater than the next
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements
    return arr  # Return the sorted array

# Example usage of Bubble Sort
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array using Bubble Sort:", sorted_arr)

# Selection Sort
def selection_sort(arr):
    """
    Selection Sort divides the array into two parts: sorted and unsorted.
    It repeatedly selects the smallest element from the unsorted part and
    moves it to the sorted part.
    """
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Outer loop for each position in the array
        min_idx = i  # Assume the current index is the minimum
        for j in range(i+1, n):  # Inner loop to find the smallest element
            if arr[j] < arr[min_idx]:  # If a smaller element is found
                min_idx = j  # Update the index of the smallest element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the smallest element with the current element
    return arr  # Return the sorted array

# Example usage of Selection Sort
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = selection_sort(arr)
print("Sorted array using Selection Sort:", sorted_arr)

# Insertion Sort
def insertion_sort(arr):
    """
    Insertion Sort builds the sorted array one element at a time by repeatedly
    picking the next element and inserting it into its correct position in the
    sorted part of the array.
    """
    for i in range(1, len(arr)):  # Start from the second element
        key = arr[i]  # The element to be inserted
        j = i-1  # Start comparing with the previous elements
        while j >= 0 and key < arr[j]:  # Shift elements to the right if they are greater than the key
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert the key into its correct position
    return arr  # Return the sorted array

# Example usage of Insertion Sort
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = insertion_sort(arr)
print("Sorted array using Insertion Sort:", sorted_arr)

# Merge Sort
def merge_sort(arr):
    """
    Merge Sort is a divide-and-conquer algorithm that splits the array into halves,
    recursively sorts each half, and then merges the sorted halves back together.
    """
    if len(arr) > 1:  # Base case: if the array has one or no elements, it is already sorted
        mid = len(arr) // 2  # Find the middle index
        L = arr[:mid]  # Split the array into the left half
        R = arr[mid:]  # Split the array into the right half

        merge_sort(L)  # Recursively sort the left half
        merge_sort(R)  # Recursively sort the right half

        i = j = k = 0  # Initialize pointers for L, R, and arr

        # Merge the sorted halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:  # If the current element in L is smaller
                arr[k] = L[i]
                i += 1
            else:  # If the current element in R is smaller
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy any remaining elements from L
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy any remaining elements from R
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr  # Return the sorted array

# Example usage of Merge Sort
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print("Sorted array using Merge Sort:", sorted_arr)

# Quick Sort
def quick_sort(arr):
    """
    Quick Sort is a divide-and-conquer algorithm that selects a pivot element,
    partitions the array into elements less than the pivot and elements greater
    than the pivot, and recursively sorts the partitions.
    """
    if len(arr) <= 1:  # Base case: if the array has one or no elements, it is already sorted
        return arr
    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot
    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort and combine the partitions

# Example usage of Quick Sort
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print("Sorted array using Quick Sort:", sorted_arr)