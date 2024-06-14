/**
 * @param {number[]} nums
 * @return {number}
 */
var minIncrementForUnique = function(nums) {
    nums.sort((a, b) => a - b);
    let ans = 0;
    let nxt = nums[0] + 1;
    for (let i = 1; i < nums.length; i++) {
        if (nxt >= nums[i]) {
            ans += (nxt - nums[i]);
            nxt++;
        } else {
            nxt = nums[i] + 1;
        }
    }
    return ans;
};