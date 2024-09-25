var TimeLimitedCache = function () {
    this.cache = new Map()
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
    const isKeyPresent = this.cache.has(key)
    if (isKeyPresent) {
        const [, prevTimeKey] = this.cache.get(key)
        clearTimeout(prevTimeKey)
    }

    const timeKey = setTimeout(() => {
        this.cache.delete(key);
    }, duration)

    this.cache.set(key, [value, timeKey])
    return isKeyPresent
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
    if (!this.cache.has(key)) {
        return -1
    }
    const [value,] = this.cache.get(key)
    return value
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
    return this.cache.size
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */