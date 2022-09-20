# https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/

def finCloseToZero(arr):
    arr.sort()
    n = len(arr)
    left = 0
    right = n-1
    min_left = 0
    min_right = n-1
    min_sum = arr[0]+arr[right]

    while(left<right):
        sum = arr[left] + arr[right]
        if( abs(sum) < abs(min_sum)):
            min_sum = sum
            min_left = left
            min_right = right
        if sum<0:
            left+=1
        else:
            right-=1
    
    print(arr[min_left] , " ", arr[min_right])



arr = [1, 60, -10, 70, -80, 85]
finCloseToZero(arr)


# Time Complexity: O(nlogn) 
# Space Complexity: O(1)