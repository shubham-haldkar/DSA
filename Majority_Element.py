
# Majority Element
# https://www.geeksforgeeks.org/majority-element/


def find_majority_element(arr):
    n = len(arr)
    dict = {}

    for i in arr:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1
    
    for i in dict:
        if(dict[i] > n/2):
            return i 
    return None




arr = [1,22,1,2,1,1,1,22,2,1,21,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2]
print(find_majority_element(arr))