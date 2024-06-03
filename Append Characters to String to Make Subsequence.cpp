class Solution {
public:
    int appendCharacters(string s, string t) {
        int t_ptr=0;
        for(int i=0;i<s.size();i++) if(s[i]==t[t_ptr]) t_ptr++;
        return t.size() - t_ptr;
    }
};