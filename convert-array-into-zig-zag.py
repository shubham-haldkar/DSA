# https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/



def convertToZigZag(arr):
    n = len(arr)
    flag = True

    for i in range(n-1):
        if(flag):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        else:
            if arr[i] < arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        flag = not flag

    print(arr)

arr = [4, 3, 7, 8, 6, 2, 1]
convertToZigZag(arr)