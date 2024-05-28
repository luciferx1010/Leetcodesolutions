class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        '''
        Function to calculate score of a character
        '''
        def get_score_character(a):
            return score[ord(a)- ord('a')]
        
        n= len(words)
        ans = 0
        
        # Iterate over all possible subsets
        for i in range(1<<n):
            score_subset = 0
            f= defaultdict(int) # frequency map of letters
            for l in letters:
                f[l]+=1
                
            flag= True # initialise to be a valid subset
            
            for j in range(n):
                if not flag:
                    break
                    
                if (1<<j)& i:
                    for c in words[j]:
                        f[c]-=1
                        if f[c] < 0: # check for invalidity
                            flag= False
                            break
                        score_subset+= get_score_character(c)
                            
            if flag: # if we reach this point, the subset is valid
                ans = max(ans, score_subset)
                
        return ans
        
        