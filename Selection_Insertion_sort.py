file = open('2_test_sorting.txt', 'r').read().strip()
l = file.split("\n")
A = [int(i) for i in l[1:]]
print(A)

n = A[0]
B = A[1:]

def min_num(A,l,n):
    min1 = 1000000
    min_index = -1
    for i in range(l,n):
        if (A[i] < min1):
            min1 = A[i]
            min_index = i
    return(min1,min_index)

def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return(A)

    def selection_sort(A,n):

        for i in range(0,n):
            num,index = min_num(A,i,n)
            swap(A,i,index)

        return (A)

    selection_sort(B,n)

file = open("Selection_sort_output.txt",'w')
file.write("Sorted Array:\n")
for x in B:
  file.write("%s\n" %x)
file.close()

n = A[0]
B = A[1:]

def insert_sort(A,n):
    for i in range(0,n-1):
        j = i
        while(j>0 and A[j-1]>A[j]):
            swap(A,j-1,j)
            j=j-1
    return (A)
insert_sort(B,n)

file = open("Insertion_sort_output.txt",'w')
file.write("Sorted Array:\n")
for x in B:
    file.write("%s\n" %x)
file.close()
