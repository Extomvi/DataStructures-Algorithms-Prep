/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
// Using Imperative programming
var filter = function(arr, fn) {
    const result = [];

    for(let i = 0; i < arr.length; i++){
        if(fn(arr[i], i)){
            result.push(arr[i]);
        }
    }
    return result;
};

// Using the filter function (declarative programming)
var filter = function(arr, fn) {
    return arr.filter(fn);  
};