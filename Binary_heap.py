file = open('5_test_heap.txt', 'r').read().strip()
l = file.split("\n")
A = [int(i) for i in l[1:]]
print(A)

n = A[0]
B = A[1:]

def swap(X,i,j):
    temp = X[i]
    X[i] = X[j]
    X[j] = temp
    return(X)

class binary_heap:

    size =0
    heap = []

    def siftdown(self,i):
        if (i>self.size):
            return
        left = 2*i
        right = left + 1
        if (left <= self.size and self.heap[i] < self.heap[left]):
            swap(self.heap,left,i)
            self.siftdown(left)
        if (right <= self.size and self.heap[i] < self.heap[right]):
            swap(self.heap,right,i)
            self.siftdown(right)

    def __init__(self,A,n):
        self.heap = [0]*(n+1)
        self.size = n
        for i in range(1,n+1):
            self.heap[i] = A[i-1]
        for i in range(n+1,0,-1):
            self.siftdown(i)


    def delMax(self):
        res = self.heap[1]
        swap(self.heap,1,self.size)
        self.size = self.size - 1
        self.siftdown(1)
        return res

heap = binary_heap(B,n)
l = []
for i in range(20):
    l.append(heap.delMax())

file = open("Max_heap_output.txt",'w')
file.write("20 Max elements:\n")
for x in l:
    file.write("%s\n" %x)
file.close()
