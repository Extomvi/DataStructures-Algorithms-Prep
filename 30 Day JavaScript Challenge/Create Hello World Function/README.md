# Day 1: Create Hello World Function

Leetcode Problem 2667: https://leetcode.com/problems/create-hello-world-function/?utm_campaign=PostD1&utm_medium=Post&utm_source=Post&gio_link_id=QPDw0kJR

Write a function createHelloWorld. It should return a new function that always returns "Hello World".
 

## Example 1:

Input: args = []

Output: "Hello World"

Explanation:

const f = createHelloWorld();

f(); // "Hello World"

The function returned by createHelloWorld should always return "Hello World".

## Example 2:

Input: args = [{},null,42]

Output: "Hello World"

Explanation:

const f = createHelloWorld();

f({}, null, 42); // "Hello World"

Any arguments could be passed to the function but it should still always return "Hello World".