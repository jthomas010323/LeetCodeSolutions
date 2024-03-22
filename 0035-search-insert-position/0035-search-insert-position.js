/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let l = 0
    let h = nums.length-1
    let m = 0
    while(l<=h){
        let m = Math.floor((l+h)/2)
        if(nums[m]==target){
            return m
        }
        if(nums[m]<target){
            l=m+1
        }
        else{
            h=m-1
        }
    }
    return l
};