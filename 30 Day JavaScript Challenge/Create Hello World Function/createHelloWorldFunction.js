/**
 * @return {Function}
 */
// Function syntax
var createHelloWorld = function() {
    return function(...args) {
        return "Hello World"
    }
};

// Arrow Syntax
var createHelloWorld = function() {
    return () => "Hello World"
};

// Arrow Syntax + Arguments
var createHelloWorld = function() {
    return (...args) => "Hello World"
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */