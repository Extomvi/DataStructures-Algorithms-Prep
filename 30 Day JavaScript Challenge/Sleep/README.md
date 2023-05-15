# Day 11: Sleep

Leetcode Problem 2621: https://leetcode.com/problems/sleep/?utm_campaign=PostD11&utm_medium=Post&utm_source=Post&gio_link_id=5Rp2Wmzo

Given a positive integer millis, write an asyncronous function that sleeps for millis milliseconds. It can resolve any value.
 

## Example 1:

Input: millis = 100

Output: 100

Explanation: It should return a promise that resolves after 100ms.

let t = Date.now();

sleep(100).then(() => {

  console.log(Date.now() - t); // 100

});

## Example 2:

Input: millis = 200

Output: 200

Explanation: It should return a promise that resolves after 200ms.