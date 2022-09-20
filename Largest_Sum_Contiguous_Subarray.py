# Largest Sum Contiguous Subarray
#   https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

 # Python program to print largest contiguous array sum

from sys import maxsize

# Function to find the maximum contiguous subarray
# and print its starting and end index
def maxSubArraySum(a,size):

	max_so_far = -maxsize - 1
	max_ending_here = 0
	# to store the starting index from where subarray starts
	start = 0  
	# to store the ending index from where subarray starts
	end = 0
	s = 0

	#iterate over array
	for i in range(0,size):
		max_ending_here += a[i]
		if max_so_far < max_ending_here:
			max_so_far = max_ending_here
			start = s
			end = i

		if max_ending_here < 0:
			max_ending_here = 0
			s = i+1

	print ("Maximum contiguous sum is %d"%(max_so_far))
	print ("Starting Index %d"%(start))
	print ("Ending Index %d"%(end))

# Driver program to test maxSubArraySum
a = [-2,1, -3, 4, -1, 2, 1, -5, 4]
maxSubArraySum(a,len(a))
