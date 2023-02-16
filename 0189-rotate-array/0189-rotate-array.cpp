class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k=k%nums.size();
        rotation(nums, 0, nums.size()-k-1);
        rotation(nums, nums.size()-k, nums.size()-1);
        rotation(nums, 0, nums.size()-1);
    }
    void rotation(vector<int>& nums, int l, int r){
        while (l<r){
            swap(nums[l], nums[r]);
            l++;
            r--;
        }
    }
};