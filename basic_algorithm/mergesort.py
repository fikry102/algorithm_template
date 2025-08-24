def merge(A, B):
    C = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    
    if i < len(A):
        C += A[i:]
    
    if j < len(B):
        C += B[j:]
    
    return C

def mergsort(A):
    n = len(A)
    if n < 2:
        return A[:]
    
    left = mergsort(A[:n // 2])
    right = mergsort(A[n // 2:])

    return merge(left, right)

if __name__ == '__main__':
    a = [7, 6, 8, 5, 2, 1, 3, 4, 0, 9, 10]
    print(a)
    print(mergsort(a))