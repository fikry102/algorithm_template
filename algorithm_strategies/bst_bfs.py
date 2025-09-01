import collections

def bst_bfs(A):

    N = len(A)
    interval = collections.deque([(float('-inf'), A[0]), (A[0], float('inf'))])

    for i in range(1, N):
        while interval:
            lower, upper = interval.popleft()
            if lower < A[i] < upper:
                interval.append((lower, A[i]))
                interval.append((A[i], upper))
                break
        
        if not interval:
            return False
    
    return True

if __name__ == "__main__":
    A = [10, 8, 11, 1, 9, 0, 5, 3, 6, 4, 12]
    print(bst_bfs(A))
    A = [10, 8, 11, 1, 9, 0, 5, 3, 6, 4, 7]
    print(bst_bfs(A))