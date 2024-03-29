class Solution
{
    public:
    vector<string> fullJustify(vector<string> &words, int maxWidth)
    {
        vector<string> ans;
        int i = 0, j = 0;
        while (i < words.size())
        {
            int charCnt = words[i].length(), spaceCnt = 0;
            j = i + 1;
            while (j < words.size() && charCnt + spaceCnt + 1 + words[j].length() <= maxWidth)
            {
                charCnt += words[j].length();
                spaceCnt++;
                j++;
            }
            int rem = maxWidth - charCnt;
            int equalDistribute = (spaceCnt == 0) ? 0 : rem / spaceCnt;
            int extraDistribute = (spaceCnt == 0) ? 0 : rem % spaceCnt;
            if (j == words.size())
            {
                equalDistribute = 1;
                extraDistribute = 0;
            }
            string s;
            for (int k = i; k < j; ++k)
            {
                s += words[k];
                if (k == j - 1)
                    break;
                for (int p = 0; p < equalDistribute; ++p)
                {
                    s.push_back(' ');
                }
                if (extraDistribute > 0)
                {
                    s.push_back(' ');
                    extraDistribute--;
                }
            }
            while (s.length() < maxWidth)
            {
                s.push_back(' ');
            }
            ans.push_back(s);
            i = j;
        }
        return ans;
    }
};