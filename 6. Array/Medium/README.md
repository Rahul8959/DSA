## 1. Two Sum: [LINK](https://leetcode.com/problems/two-sum/description/)
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

## 2. Sort An Array of 0s, 1s and 2s:  [LINK](https://www.naukri.com/code360/problems/sort-an-array-of-0s-1s-and-2s_892977)

You have been given an array/list 'arr' consisting of 'n' elements.
Each element in the array is either 0, 1 or 2.

Sort this array/list in increasing order.

Do not make a new array/list. Make changes in the given array/list.

Example :
Input: 'arr' = [2, 2, 2, 2, 0, 0, 1, 0]

Output: Final 'arr' = [0, 0, 0, 1, 2, 2, 2, 2]

Explanation: The array is sorted in increasing order.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
8
2 2 2 2 0 0 1 0

Sample Output 1:
0 0 0 1 2 2 2 2

Explanation of sample input 1 :
The initial array 'arr' is [2, 2, 2, 2, 0, 0, 1, 0].

After sorting the array in increasing order, 'arr' is equal to:
[0, 0, 0, 1, 2, 2, 2, 2]

## 3. Majority Element: [LINK](https://www.naukri.com/code360/problems/majority-element_6783241?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems)
You are given an array 'a' of 'n' integers.

A majority element in the array ‘a’ is an element that appears more than 'n' / 2 times.

Find the majority element of the array.

It is guaranteed that the array 'a' always has a majority element.

Example:

Input: ‘n’ = 9, ‘a’ = [2, 2, 1, 3, 1, 1, 3, 1, 1]

Output: 1

Explanation: The frequency of ‘1’ is 5, which is greater than 9 / 2.
Hence ‘1’ is the majority element.

## 4. Maximum Subarray: [LINK](https://leetcode.com/problems/maximum-subarray/description/)
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]

Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]

Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]

Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

## 5. Best time to buy and sell stock: [LINK](https://www.naukri.com/code360/problems/stocks-are-profitable_893405?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTabValue=PROBLEM)
You are given an array/list 'prices' where the elements of the array represent the prices of the stock as they were yesterday and indices of the array represent minutes. Your task is to find and return the maximum profit you can make by buying and selling the stock. You can buy and sell the stock only once.

Note:

You can’t sell without buying first.
For Example:

For the given array [ 2, 100, 150, 120],

The maximum profit can be achieved by buying the stock at minute 0 when its price is Rs. 2 and selling it at minute 2 when its price is Rs. 150.
So, the output will be 148.

## 6. Alternate Numbers: [LINK](https://leetcode.com/problems/rearrange-array-elements-by-sign/description/)
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should return the array of nums such that the the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

Example 1:

Input: nums = [3,1,-2,-5,2,-4]

Output: [3,-2,1,-5,2,-4]
Explanation:

The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].

The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].

Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  

## 7. Array Leader: [LINK](https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1)
Given an array arr of n positive integers, your task is to find all the leaders in the array. An element of the array is considered a leader if it is greater than all the elements on its right side or if it is equal to the maximum element on its right side. The rightmost element is always a leader.

Examples

Input: n = 6, arr[] = {16,17,4,3,5,2}

Output: 17 5 2

Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.

## 8. Longest Successive Elements: [LINK](https://www.naukri.com/code360/problems/longest-successive-elements_6811740)
There is an integer array ‘A’ of size ‘N’.
A sequence is successive when the adjacent elements of the sequence have a difference of 1.

You must return the length of the longest successive sequence.

Note:

You can reorder the array to form a sequence. 
For example,

Input:

A = [5, 8, 3, 2, 1, 4], N = 6

Output:

5

Explanation: 

The resultant sequence can be 1, 2, 3, 4, 5.    

The length of the sequence is 5.

## 9. Set Metrics Zero [LINK](https://leetcode.com/problems/set-matrix-zeroes/description/)
You are given a matrix 'MATRIX' of dimension 'N' x 'M'. Your task is to make all the elements of row 'i' and column 'j' equal to 0 if any element in the ith row or jth column of the matrix is 0.

Note:

The number of rows should be at least 1.

The number of columns should be at least 1.

For example, refer to the below matrix illustration: 

1 1 1      1 0 1
1 0 1  =>  0 0 0
1 1 1      1 0 1

## 10. Rotated Matrix By 90 Degree [LINK](https://www.naukri.com/code360/problems/rotate-the-matrix_6825090)
You are given a square matrix ‘Mat’ of size ‘N’. You need to rotate ‘Mat’ by 90 degrees in the clockwise direction.

Note:

You must rotate the matrix in place, i.e., you must modify the given matrix itself. You must not allocate another square matrix for rotation.
For example

When,
‘N’ = 2 and ‘Mat’ = {{1, 2}, {3, 4}}, we must modify ‘Mat’ to {{3, 1}, {4, 2}}.

## 11. Next Permutaion [LINK](https://leetcode.com/problems/next-permutation/description/)
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].

Similarly, the next permutation of arr = [2,3,1] is [3,1,2].

While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.