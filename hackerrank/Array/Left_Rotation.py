from collections import deque

def rotateLeft(d, arr):
    # Write your code here
    array = deque(arr)
    for i in range(d):
        a = array.popleft()
        array.append(a)
    
    return array
        
    
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)
    
    print(result)