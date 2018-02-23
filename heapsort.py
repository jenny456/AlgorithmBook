def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left child = 2*i + 1
    r = 2 * i + 2     # right child = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function 
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)
 
# Driver code to test above
arr = []
n=int(input("enter number of elements"))
print("enter elements")
for i in range(n):
    arr.append(int(input()))
heapSort(arr)
n = len(arr)
print (" The Sorted array is")
for i in range(n):
    print ("%d" %arr[i])
