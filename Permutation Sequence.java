class Solution {
    public String getPermutation(int n, int k) {
        boolean[] map=new boolean[n];
        ll=new ArrayList<>();
        rec(n,k,"",map);
        return ll.get(ll.size()-1);
    }
    static List<String> ll;
    public static void rec(int n,int k,String ans,boolean[] map){
        if(ans.length()==n){
            ll.add(ans);
            return;
        }
        if(ll.size()==k){
            return;
        }
        for(int i=1;i<=n;i++){
            if(map[i-1]==false){
                map[i-1]=true;
                rec(n,k,ans+i,map);
                map[i-1]=false;
            }
        }
    }
}