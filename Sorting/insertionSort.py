def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j>=0 and A[j]>key:
            A[j+1] = A[j]
            j-=1
        A[j+1] = key

"""
Details of the sorting technique:

from the code it can be seen that the time complexity of insertion sort is 0(n^2) : This is for the worst case
The best case will be when the list is already sorted in ascending order (in this case)
_____________________________________________________________
|Case        |   Scenario                        |Complexity |
|------------|-----------------------------------|-----------|
|Best Case   |   The list is already sorted      |   O(n)    |
|------------|-----------------------------------|-----------|
|Worst Case  |   The list is soreted in reverse  |  O(n^2)   |
|------------|-----------------------------------|-----------|
|Average Case|   The list not sorted             |   O(n^2)  |
|____________|___________________________________|___________|

"""




if __name__ == '__main__':
    l = [6,35,7,8,4,7]
    print(f"The list before sorting : {l}")
    insertion_sort(l)
    print(f"The list sorted using Insertion Sort : {l}")