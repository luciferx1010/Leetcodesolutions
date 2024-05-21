class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        nm = n*m
        f = list(range(nm))
        
        def find(x):
            if f[x] != x:
                f[x] = find(f[x])

            return f[x]

        def merge(u, v):
            fu, fv = find(u), find(v)
            if fu < fv:
                f[fu] = fv
            elif fv < fu:
                f[fv] = fu

        # mp is an array, mp[i] stores the [y, x] which has the distance i to the nearest theif
        mp = [[]]
        for y in range(n):
            for x in range(m):
                if grid[y][x]:
                    mp[0].append([y, x])
                    grid[y][x] = None

        # calculate the mp by using BFS
        while grid[0][0] is not None and grid[-1][-1] is not None:
            que = mp[-1]
            que2 = []
            mp.append(que2)

            for y, x in que:
                for y1, x1 in [y+1, x], [y-1, x], [y, x+1], [y, x-1]:
                    if 0 <= y1 < n and 0 <= x1 < m and grid[y1][x1] is not None:
                        que2.append([y1, x1])
                        grid[y1][x1] = None

        que = mp.pop()
        for y, x in que:
            grid[y][x] = 0

        # Use Union-find to see if there's a router from start to end
        for y in range(n):
            for x in range(m):
                if grid[y][x] is not None:
                    idx = y*m+x
                    if y+1 < n and grid[y+1][x] is not None:
                        merge(idx, idx+m)
                    if x+1 < m and grid[y][x+1] is not None:
                        merge(idx, idx+1)

        if find(0) == nm-1:
            return len(mp)

        # In each step, recovered the [y, x] in mp[-1], which is the nodes with the longest distance to the theif.
        # If there's a valid path, break. Then the answer is this len(mp)
        while mp:
            que = mp.pop()
            for y, x in que:
                grid[y][x] = 0
                idx = y*m+x
                for y1, x1 in [y+1, x], [y-1, x], [y, x+1], [y, x-1]:
                    if 0 <= y1 < n and 0 <= x1 < m and grid[y1][x1] is not None:
                        merge(idx, y1*m+x1)
            if find(0) == nm-1:
                break

        return len(mp)