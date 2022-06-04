# https://www.geeksforgeeks.org/merging-intervals/

def MergeIntervals(arr):
    arr.sort(key = lambda x: x[0])
    print(arr)
    start = arr[0][0]
    end = arr[0][1]
    new_arr = []
    n = []
    for i in range(1,len(arr)):
 
        if(end >= arr[i][0] and end < arr[i][1]  )  :
            end =  arr[i][1] 
        elif (end >= arr[i][0] and end >= arr[i][1]  ):
            end = end
        elif end < arr[i][0] :
            n = []
            n.append(start)
            n.append(end)
            new_arr.append(n)
            start = arr[i][0]
            end = arr[i][1]
   
    
    n = []
    n.append(start)
    n.append(end)
    new_arr.append(n)

    print("Merge Inrtervals are ", new_arr)





arr = [[6, 8], [1, 2], [2, 3], [4, 7]]
arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
MergeIntervals(arr)