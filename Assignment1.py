#Avinna Bhattarai 
#Using the algorithm from the book
A= [7,8,5,4,3]
n = len(A)
for i in range(1, n):
        key = A[i]
        j = i - 1
        # Move elements of A[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

print(A)