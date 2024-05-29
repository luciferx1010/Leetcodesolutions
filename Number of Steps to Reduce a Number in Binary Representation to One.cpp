class Solution {
public:
    int numSteps(string s) {
        int count=0;
        while(s!="1"){
            if(s.back()=='0'){ //1100-> 
                s.pop_back();
            }
            else{
                int i=s.size()-1;
                while(i>=0 && s[i]=='1'){
                    s[i]='0';
                    i--;
                }
                if(i>=0){
                    s[i]='1';
                } //111->1000
                else{
                    s.insert(s.begin(),'1');
                }
            }
            count++;
        }
        return count;
    }
};