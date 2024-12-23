""" Positive Array

You are given an array A of length N containing only positive integers.
You must perform the following operation any number of times such that the mean of the array is an integer:
Select any index i and add any positive integer at that index.
Find the minimum sum of array A.
 
Note
Mean = Sum of all elements / Number of elements.
1-based indexing is used.
 
Function Description
In the provided code snippet, implement the provided positiveArray(...) method to find the minimum sum of the array A. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

Input Format
The first line contains an integer N, denoting the size of the array.
The second line contains N space-separated integers of array A, denoting the array elements.

Sample Input
4                      -- denotes N
3 1 8 9             -- denotes A[i]
 
Constraints
0 < N <= 105
0 < A[i] <= 103

Output Format
The output contains a single integer denoting the minimum sum of the array A.

Sample Output
24

Explanation
A = [3, 1, 8, 9]
One of the possible arrays is [5, 2, 8, 9]
This can be achieved by adding 2 at the 1st and 1 at the 2nd indices.
The mean is = (5 + 2 + 8 + 9) / 4 = 6, which is an integer.
The minimum sum is 24, and it can be proven that it is the minimum that can be achieved.
Hence, the output is 24."""

def positiveArray(N, A):

    # this is default OUTPUT. You can change it.
    result = 0

    # write your Logic here:

    for num in A:
        result += num

    while result % N !=0:
        result +=1
    return result

# INPUT [uncomment & modify if required]

N = int(input())

temp = input().split()
A = []
for i in range(N):
    A.append(int(temp[i]))

# OUTPUT [uncomment & modify if required]
print(positiveArray(N,A))


