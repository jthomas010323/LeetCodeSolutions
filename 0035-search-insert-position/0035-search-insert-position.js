/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    const findIt = nums.findIndex(x => x === target);
    if (findIt !== -1) return findIt;

    let count = nums.length;
    for (let i; (i = nums.pop()); ) {
        if (i > target) {
            count--;
            continue;
        } else {
            return count; 
        }
    }

    return 0;
};