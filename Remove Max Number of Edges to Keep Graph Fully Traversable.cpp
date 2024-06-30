class DSU {
	vector<int>parent, size;
public:

	DSU(int n) {
        size.resize(n + 1, 0);
		parent.resize(n + 1, 0);
		for(int i = 0; i <= n; i++) {
			parent[i] = i;

		}
	}

	bool isSame(int u, int v) {
        return findPar(u) == findPar(v);
    }
	
	int findPar(int node) {
		if(node == parent[node]) return node;
		return parent[node] = findPar(parent[node]);
	}

	int unionBySize(int u, int v) {
		int ulp_u = findPar(u);
		int ulp_v = findPar(v);
		if(ulp_u == ulp_v) return 0;
		if(size[ulp_u] < size[ulp_v]) {
			parent[ulp_u] = ulp_v;
			size[ulp_v] += size[ulp_u];
		} 
		else {
			parent[ulp_v] = ulp_u;
			size[ulp_u] += size[ulp_v];
		}
        return 1;
	}
};


class Solution {
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {

        DSU d1(n);
        DSU d2(n);

        int alice = 0, bob = 0, c = 0;

        sort(edges.rbegin(), edges.rend());

        for(auto it : edges) {
            int t = it[0], u = it[1], v = it[2];

            if(t == 3) {
                int f1 = d1.unionBySize(u, v);
                int f2 = d2.unionBySize(u, v);
                alice += f1;
                bob += f2;
                if(f1 | f2) c++;
            }
            else if(t == 2) {
                int f2 = d2.unionBySize(u, v);
                bob += f2;
                c += f2;
            }
            else {
                int f1 = d1.unionBySize(u, v);
                alice += f1;
                c += f1;
            }
        }

        if(alice != n- 1 || bob != n - 1) return -1;

        return edges.size() - c;
    }
};