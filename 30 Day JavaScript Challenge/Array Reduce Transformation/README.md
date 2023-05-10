# Day 6: Array Reduce Transformation

Leetcode Problem 2626: https://leetcode.com/problems/array-reduce-transformation/?utm_campaign=PostD6&utm_medium=Post&utm_source=Post&gio_link_id=nPN45jD9

Given an integer array nums, a reducer function fn, and an initial value init, return a reduced array.

A reduced array is created by applying the following operation: val = fn(init, nums[0]), val = fn(val, nums[1]), val = fn(val, nums[2]), ... until every element in the array has been processed. The final value of val is returned.

If the length of the array is 0, it should return init.

Please solve it without using the built-in Array.reduce method.



## Example 1:

Input: 

nums = [1,2,3,4]

fn = function sum(accum, curr) { return accum + curr; }

init = 0

Output: 10

Explanation:

initially, the value is init=0.

(0) + nums[0] = 1

(1) + nums[1] = 3

(3) + nums[2] = 6

(6) + nums[3] = 10

The final answer is 10.

## Example 2:

Input: 

nums = [1,2,3,4]

fn = function sum(accum, curr) { return accum + curr * curr; }

init = 100

Output: 130

## Explanation:

initially, the value is init=100.

(100) + nums[0]^2 = 101

(101) + nums[1]^2 = 105

(105) + nums[2]^2 = 114

(114) + nums[3]^2 = 130

The final answer is 130.

## Example 3:

Input: 

nums = []

fn = function sum(accum, curr) { return 0; }

init = 25

Output: 25

Explanation: For empty arrays, the answer is always init.