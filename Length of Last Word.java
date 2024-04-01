import java.util.StringTokenizer;

public class Solution {
    public int lengthOfLastWord(String s) {
        StringTokenizer st = new StringTokenizer(s);
        String lastWord = "";
        while (st.hasMoreTokens()) {
            lastWord = st.nextToken();
        }
        return lastWord.length();
    }
}