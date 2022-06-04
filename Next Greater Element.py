#Next Greater Element

from inspect import stack


def next_greater_element(arr):
    stack = []
    stack.append(arr[0])
    
    for i in range(1,len(arr)) :
        next = arr[i]
        if stack:
            el = stack.pop()
            while el < next:
                print(str(el) + " -- " + str(next))
                if not stack:
                    break
                el = stack.pop()
 
            if el>next:
                stack.append(el)
        stack.append(next)

    for i in stack:
        print(i , " -- -1" )


arr =  [11, 13, 21, 3]
next_greater_element(arr)