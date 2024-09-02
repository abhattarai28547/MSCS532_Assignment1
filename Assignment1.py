#Avinna Bhattarai 
#Write a Python program for the Insertion Sort Algorithm that sorts in monotonically decreasing order.

#Method for Decreasing Insertion Sort

def insertion_sort_decreasing(A):
    #setting n as number of elements in the given array
    n = len(A)

    for i in range(1, n):
            key = A[i]
            j = i - 1
            # Moving elements of A[0..i-1], that are greater than key, to one position ahead of their current position
            while j >= 0 and A[j] < key:
                A[j + 1] = A[j]
                j -= 1
            A[j + 1] = key


#main 
 #This is an example array(The numerical elements can be changed as desired)
A= [56,46,77,23,99]
print("Given array: ",A)
insertion_sort_decreasing(A)
print("Sorted array in decreasing order: ",A)