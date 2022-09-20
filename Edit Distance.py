# Given two strings str1 and str2 and below operations that can be performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.  

# Insert
# Remove
# Replace
# All of the above operations are of equal cost. 

# https://www.geeksforgeeks.org/edit-distance-dp-5/


def editDistance (str1, str2, m,n):
    dp = [[0 for x in range (n+1)] for x in range (m+1)]

    for i in range(m+1):
        for j in range(n+1):
            # if first string is empty then min operation is j
            if i==0:
                dp[i][j] = j
            # if second string is empty then min operation is i
            elif j==0:
                dp[i][j] = i
            # Check for the character at i of str1 and char at j of str2
            elif(str1[i-1] == str2[j-1]):
                dp[i][j] = dp[i-1][j-1] # coy diagonal element
            # else copy the min of top,left or diagonal and add 1
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace

    return dp[m][n]




str1 = "food"
str2 = "money"
 
print(editDistance(str1, str2, len(str1), len(str2)))