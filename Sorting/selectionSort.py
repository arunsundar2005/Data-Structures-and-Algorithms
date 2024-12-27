from insertionSort import insertion_sort



def selection_sort(A):
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]


"""
Details of the sorting technique:

from the code it can be seen that the time complexity of insertion sort is 0(n^2)

"""




if __name__=='__main__':
    l = [5,4,6,1,3]
    print(f"The list before sorting : {l}")
    selection_sort(l)
    print(f"The sorted list using Selectio Sort : {l}")