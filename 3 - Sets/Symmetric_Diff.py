# Set Functions:
#   add() - add single element      update() - only works for iterable objects
#   discard(), remove() - take a single value as an argument and removes that value
#   If the value is not present, discard() does nothing, but remove() will raise a KeyError exception.
#   union(), intersection() and difference()


def symm_diff(M, N):
    M = set(M)
    N = set(N)
    U = M.union(N)
    X = M.intersection(N)
    return list(U-X)

if __name__ == '__main__':
    n = int(input())
    M = list(map(int, input().split()))
    n = int(input())
    N = list(map(int, input().split()))

    result = symm_diff(M, N)
    result.sort()
    print(*result, sep='\n')
