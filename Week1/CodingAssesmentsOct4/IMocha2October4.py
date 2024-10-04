""" Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Input Format
The first line contains a String array word1
The second line contains a String array word2

Sample Input
"ab" "c"      -- denotes word1
"a" "bc"  -- denotes word2

Output Format
The output contains an integer value 1 or 0 denoting whether the concatenated arrays are equal or not

Sample Output
1

Explanation
 
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true and print the output 1. """

#INPUT [uncomment & modify if required]  

#write your Logic here:  
word1 = "".join(input().split(" "))
word2 = "".join(input().split(" "))

#OUTPUT [uncomment & modify if required]  
print(1 if word1 == word2 else 0)
