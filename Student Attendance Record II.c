#define MODVAL 1000000007ULL

int checkRecord(int n) {        
	unsigned long long F[n+3]; /* Number of records w/o 'A' */
	F[0] = 1; /* empty record */
	F[1] = 2; /* 'P' or 'L' */
	F[2] = 4; /* 'PL', 'PP', "LP', or 'LL' */
	for (int i=3; i<=n; i++) F[i] = (F[i-3] + F[i-2] + F[i-1]) % MODVAL;
	
    unsigned long long ans = F[n]; /* A record wo absence is eligble */
    /* absent on day k => add records of length k-1 * records n-k-1 */
	for (int k=0; k<n; k++) ans = (ans + F[k] * F[n-k-1]) % MODVAL;
	return ans;
}