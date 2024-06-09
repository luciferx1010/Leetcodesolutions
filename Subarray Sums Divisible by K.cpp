class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        int n = nums.size(),sum =0;
        vector<int>pre(n+1,0);
        unordered_map<int,int>mp;
        mp[0] = 1;
        int ans =0;
        for(int i=0;i<n;i++){
            sum = ((sum + nums[i]) % k + k) % k;
            if(mp.count(sum)){
                ans += mp[sum];
            }
            mp[sum]++;

        }
        return ans;
    }
};