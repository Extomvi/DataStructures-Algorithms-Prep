/**
 * @return {Function}
 */
// Function
var createHelloWorld = function() {
    return function(...args) {
        return "Hello World"
    }
};

// Arrow
var createHelloWorld = function() {
    return () => "Hello World"
};

// Arrow + Arguments
var createHelloWorld = function() {
    return (...args) => "Hello World"
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */