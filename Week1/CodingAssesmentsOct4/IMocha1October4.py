""" You are given an array having N elements and an integer K.

You have to write a program to find the smallest number greater than K which is not present in the given array.

Example
If the array is A = [ 2, 5, 7, 9, 21, 34] and K = 20
The output will be 22.
22 will be the smallest number greater than K=20 which is not present in the given array.

Input Format
The code provided handles the input and stores them in variables for you.
The first line contains an integer N denoting the size of the array.
The next N lines contain elements of array A.
The next line contains an integer, K.

Sample Input
5        -- denotes N
1        -- denotes elements of Array N
4
5
2
7
4        -- denotes K


Output Format
The output contains an integer denoting the smallest number greater than K which is not present in the given array.

Sample Output
6
Explanation
The array is [1,4,5,2,7] and K=4
The smallest element which is greater than K = 4 and not present in the array is 6.
Hence the output is 6. """

#INPUT [uncomment & modify if required]  
sampleInput = int(input()) 
result = -404; 
arr = []

for i in range(0, sampleInput):
    arr.append(int(input()))

kv = int(input())

#write your Logic here:  
def notInArray(li, k):
    mapped = {i:True for i in li if i > k}
    print(mapped)
    n = 1
    while(True):
        if not mapped.get(k+n):
            return k+n
        n+=1


#OUTPUT [uncomment & modify if required]  
print(notInArray(arr,kv))