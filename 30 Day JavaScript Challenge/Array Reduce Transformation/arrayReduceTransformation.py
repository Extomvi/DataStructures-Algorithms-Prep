/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let result = init;

    for(const val of nums){
        result = fn(result, val);
    }
    return result
};

// Using the forEach method
var reduce = function(nums, fn, init) {
    let result = init;

    nums.forEach((val) => {
        result = fn(result, val)
    });
    return result
};

// Using .reduce inbuilt function
var reduce = function(nums, fn, init) {
    return nums.reduce(fn, init);
};