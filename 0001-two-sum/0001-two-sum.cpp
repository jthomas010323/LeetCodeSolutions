class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int ,int> map;
        vector<int> result;
        for(int i=0; i<nums.size();i++){
            int secondvalue=target-nums[i];
            
            
            if(map.find(secondvalue)!=map.end())
            {
                return {map[secondvalue], i};
                    }
        map[nums[i]]=i;
        }
return {};
    }
};