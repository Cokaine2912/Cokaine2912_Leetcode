/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        let greet = "Hello World"
        return greet
        
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */