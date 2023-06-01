# Day 27: Event Emitter

Leetcode Problem 2694: https://leetcode.com/problems/event-emitter/?utm_campaign=PostD27&utm_medium=Post&utm_source=Post&gio_link_id=lPQDyGjR

Design an EventEmitter class. This interface is similar (but with some differences) to the one found in Node.js or the Event Target interface of the DOM. The EventEmitter should allow for subscribing to events and emitting them.

Your EventEmitter class should have the following two methods:

* subscribe - This method takes in two arguments: the name of an event as a string and a callback function. This callback function will later be called when the event is emitted.
An event should be able to have multiple listeners for the same event. When emitting an event with multiple callbacks, each should be called in the order in which they were subscribed. An array of results should be returned. You can assume no callbacks passed to subscribe are referentially identical.

The subscribe method should also return an object with an unsubscribe method that enables the user to unsubscribe. When it is called, the callback should be removed from the list of subscriptions and undefined should be returned.

* emit - This method takes in two arguments: the name of an event as a string and an optional array of arguments that will be passed to the callback(s). If there are no callbacks subscribed to the given event, return an empty array. Otherwise, return an array of the results of all callback calls in the order they were subscribed.
 

## Example 1:

Input: actions = ["EventEmitter", "emit", "subscribe", "subscribe", "emit"], values = [[], ["firstEvent", "function cb1() { return 5; }"],  ["firstEvent", "function cb1() { return 5; }"], ["firstEvent"]]

Output: [[],["emitted",[]],["subscribed"],["subscribed"],["emitted",[5,6]]]

Explanation: 

const emitter = new EventEmitter();

emitter.emit("firstEvent"); // [], no callback are subscribed yet

emitter.subscribe("firstEvent", function cb1() { return 5; });

emitter.subscribe("firstEvent", function cb2() { return 6; });

emitter.emit("firstEvent"); // [5, 6], returns the output of cb1 and cb2

## Example 2:

Input: actions = ["EventEmitter", "subscribe", "emit", "emit"], values = [[], ["firstEvent", "function cb1(...args) { return args.join(','); }"], ["firstEvent", [1,2,3]], ["firstEvent", [3,4,6]]]

Output: [[],["subscribed"],["emitted",["1,2,3"]],["emitted",["3,4,6"]]]

Explanation: Note that the emit method should be able to accept an OPTIONAL array of arguents.

const emitter = new EventEmitter();

emitter.subscribe("firstEvent, function cb1(...args) { return args.join(','); });

emitter.emit("firstEvent", [1, 2, 3]); // ["1,2,3"]

emitter.emit("firstEvent", [3, 4, 6]); // ["3,4,6"]

## Example 3:

Input: actions = ["EventEmitter", "subscribe", "emit", "unsubscribe", "emit"], values = [[], ["firstEvent", "(...args) => args.join(',')"], ["firstEvent", [1,2,3]], [0], ["firstEvent", [4,5,6]]]

Output: [[],["subscribed"],["emitted",["1,2,3"]],["unsubscribed",0],["emitted",[]]]

Explanation:

const emitter = new EventEmitter();

const sub = emitter.subscribe("firstEvent", (...args) => args.join(','));

emitter.emit("firstEvent", [1, 2, 3]); // ["1,2,3"]

sub.unsubscribe(); // undefined

emitter.emit("firstEvent", [4, 5, 6]); // [], there are no subscriptions