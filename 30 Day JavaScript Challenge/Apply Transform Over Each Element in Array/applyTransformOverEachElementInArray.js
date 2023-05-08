/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
// First method
var map = function(arr, fn) {
    const result = [];
    for (const i in arr){
        result.push(fn(arr[i], Number(i)));
    }
    return result
};

// Second method
var map = function(arr, fn) {
    const result = new Array(arr.length);

    for (const i in arr){
        result[i] = fn(arr[i], Number(i));
    }
    return result;
};

// Or using the map function
var map = function(arr, fn) {
    
    return arr.map(fn);
};