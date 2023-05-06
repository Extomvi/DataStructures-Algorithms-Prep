/**
 * @param {number} n
 * @return {Function} counter
 */
// Method 1
var createCounter = function(n) {
    return function() {
        return n++;        
    };
};
// Method 2
var createCounter = function(n) {
    let count = n
    return function() {
        return count++;        
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */