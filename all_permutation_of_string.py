# Write a program to print all permutations of a given string

# Python program to print all permutations with
# duplicates allowed

def toString(List):
	return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.


def permute(a,left,right):
    print(left, " ", right , " " , a)
    if left==right:
        print (toString(a))
    else:
        for i in range(left,right):
            print(i)
            print(a[left],a[i])
            a[left],a[i] = a[i],a[left]
            permute(a,left+1,right)
            a[left],a[i] = a[i],a[left]    # backtrack 
            
 

# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n)

# This code is contributed by Bhavya Jain
