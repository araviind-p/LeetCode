/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    num = args.length
    return num
};

/**
 * argumentsLength(1, 2, 3); // 3
 */