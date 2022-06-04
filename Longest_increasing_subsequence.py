# Longest Increasing Subsequence | DP-3
# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/


 


def LIS(arr):
    n = len(arr)
 
    lis = [1]
    for i in range(1,n):
        lis.append(1)
        for j in range(0,i):
            # print(temp , " " , arr[i] , arr[j])
            if(arr[i] > arr[j]):
                lis[i] = max(lis[j]+1 , lis[i] )
                
    print( max(lis))



def LIS_recursion(arr,n):
 
    # Base Case
    if n == 1:
        return 1
 
    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1
 
    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
       IF arr[i-1] is smaller than arr[n-1], and max ending with
       arr[n-1] needs to be updated, then update it"""
    for i in range(1, n):
        res = LIS_recursion(arr, i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res + 1
 
    # Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
 
 
    return maxEndingHere
 

arr = [3, 10, 2, 11]
# LIS(arr)
 
print(LIS_recursion(arr, len(arr)))
