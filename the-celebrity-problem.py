# https://www.geeksforgeeks.org/the-celebrity-problem/


N = 8

# Person with 2 is celebrity
MATRIX = [[0, 0, 1, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 0],
           [0, 0, 1, 0]]
 
 
def knows(a, b):
    return MATRIX[a][b]

def celebrityFind():
    n = len(MATRIX)
    celebrity = 0
    for i in range(1,n-1):
        second = i        
        if(knows(celebrity,second) and not knows(second,celebrity)):
            celebrity = second
    
    c1=0
    c2=0

    # Check the id is really the
    # celebrity
    for i in range(n):
        if (i != celebrity):
            c1 += knows(celebrity, i)
            c2 += knows(i, celebrity)

    # If the person is known to
    # everyone.
    if (c1 == 0 and c2 == n - 1):
        return (celebrity)
    return -1






print(celebrityFind())