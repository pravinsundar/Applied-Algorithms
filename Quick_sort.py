import random

file = open('4_test_sorting.txt', 'r').read().strip()
l = file.split("\n")
A = [int(i) for i in l[1:]]
print(A)

n = A[0]
B = A[1:]

def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return(A)

def partition(A,low,high):
    i= low+1
    j = high-1
    pivot = A[low]
    while(i<j):
        while(A[i]<= pivot):
            i = i+1
        while(A[j]>= pivot):
            j = j-1
        if (i<j):
            swap(A,i,j)
    swap(A,low,j)
    return (j)

def quick_sort(A,low,high):
    if (low<high-1):
        i = random.randint(low,high)
        swap(A,low,i)
        p=partition(A,low,high)
        quick_sort(A,low,p)
        quick_sort(A,p+1,high)

quick_sort(B,0,n-1)
print(B)

file = open("Quick_sort_output.txt",'w')
file.write("Sorted Array:\n")
for x in B:
    file.write("%s\n" %x)
file.close()
