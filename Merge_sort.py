file = open('3_test_sorting.txt', 'r').read().strip()
l = file.split("\n")
A = [int(i) for i in l[1:]]
print(A)


n = A[0]
B = A[1:]

def merge_sort(a,aux,low,high):
    if((high-low) <=1):
        return
    mid = int((low + high)/2)

    merge_sort(a,aux,low,mid)

    merge_sort(a,aux,mid,high)

    merge(a,aux,low,mid,high)

def merge(a,aux,low,mid,high):

    for l in range(low,high):
        aux[l] = a[l]
    i = low
    j = mid
    k = low
    while(i<mid and j<high):
        if (aux[i] <= aux[j]):
            a[k] = aux[i]
            k = k+1
            i = i+1
        else:
            a[k] = aux[j]
            k = k+1
            j = j+1
    while(i < mid):
        a[k] = aux[i]
        k = k+1
        i = i+1
    while(j < high):
        a[k] = aux[j]
        k = k+1
        j = j+1

c = [0]*n
merge_sort(B,c,0,n)

print(B)
file = open("Merge_sort_output.txt",'w')
file.write("Sorted Array:\n")
for x in B:
    file.write("%s\n" %x)
file.close()
