"""Element Removal

You are given an integer array A and an integer K.
Remove the minimum number of elements such that the frequency of each element is divisible by K.

Find the minimum number of elements removed.

Function Description
In the provided code snippet, implement the provided elementRemoval(...) method using the variables to find the minimum number of elements removed. You can write your code in the space below the phrase “WRITE YOUR LOGIC HERE”.

There will be multiple test cases running so the Input and Output should match exactly as provided.
The base Output variable result is set to a default value of -404 which can be modified. Additionally, you can add or remove these output variables.

Input Format
The first line contains an integer N, denoting the size of the string array.
The second line contains an integer, K.
The third line contains N space-separated integers of array A, denoting the elements of the array.

Sample Input
5                          -- denotes N
2                          -- denotes K
1 1 1 2 2              -- denotes A[i]

Constraints
1 <= N <= 100000
1 <= K <= 100000

Output Format
The output contains a single integer denoting the minimum number of elements removed.

Sample Output
1
 
Explanation
K = 2
A = [1, 1, 1, 2, 2]
Remove one 1 from the array.
A = [1, 1, 2, 2]
The frequency of each element is divisible by 2.
The minimum number of elements removed is 1.
Hence, the output is 1."""

def elementRemoval(N, K, A):

    # this is default OUTPUT. You can change it.

    result = 0

    # write your Logic here:

    f = {}

    for value in A:
        if value in f:
            f[value] += 1
        else:
            f[value] = 1

    for key in f.keys():
        result += f[key] % K
    return result

# INPUT [uncomment & modify if required]
N = int(input())
K = int(input())

temp = input().split()

A = []

for i in range(N):
    A.append(int(temp[i]))

# OUTPUT [uncomment & modify if required]
print(elementRemoval(N,K,A))