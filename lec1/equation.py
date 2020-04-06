#A,B,C = [int(x) for x in input().split()] # input().split() --- > ['5', '4', '3']
# '5 4 3' -- > ['5', '4', '3'] -- > [5, 4, 3] --> A = 5 B =4 C = 3

def linear(B,C):
    if B == 0:
        # C == 0
        return 0 
    else:
        # Bx + C == 0
        return 1

def quadratic(A,B,C):
    D = B**2 - 4*A*C
    if D > 0:
        return 2
    elif D == 0:
        return 1
    else:
        return 0


def solve(A,B,C):
    if A == 0:
        return linear( B,C)  
    else:
        return quadratic(A,B,C)
        
        

if __name__ == '__main__':
    A,B,C = map(int, input().split())
    print(solve(A,B,C))

# Процесс создания юнитов - декомпозиция кода


