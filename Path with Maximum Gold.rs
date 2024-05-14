impl Solution {
    pub fn bt(grid: &mut Vec<Vec<i32>>, n: usize, m: usize, i: usize, j: usize) -> i32 {
        if n <= i || m <= j || grid[i][j] == 0 {
            return 0;
        }
        let ds: [(isize, isize); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];
        let cur = grid[i][j];
        grid[i][j] = 0;
        let res = ds.iter().fold(0, |acc, &(di, dj)| {
            let nb = Self::bt(
                grid,
                n,
                m,
                i.checked_add_signed(di).unwrap_or(n),
                j.checked_add_signed(dj).unwrap_or(m),
            );
            acc.max(nb)
        });
        grid[i][j] = cur;
        res + cur
    }

    pub fn get_maximum_gold(mut grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let m = grid[0].len();
        let mut ans: i32 = 0;
        for i in 0..n {
            for j in 0..m {
                ans = ans.max(Self::bt(&mut grid, n, m, i, j));
            }
        }
        ans
    }
}