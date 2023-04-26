class Solution {
    public int[] solution(int[][] arr) {
        return dfs(arr, arr.length, 0, 0);
    }

    public int[] dfs(int[][] arr, int level, int x, int y) {
        int target = arr[x][y];
        if (level == 1 || check(arr, level, x, y)) {
            if (target == 0) {
                return new int[] {1, 0};
            }
            return new int[] {0, 1};
        }

        int[] a = new int[] {0, 0};
        int next_level = level / 2;
        int[] res = dfs(arr, next_level, x, y);
        a[0] = a[0] + res[0];
        a[1] = a[1] + res[1];

        res = dfs(arr, next_level, x+next_level, y);
        a[0] = a[0] + res[0];
        a[1] = a[1] + res[1];

        res = dfs(arr, next_level, x, y+next_level);
        a[0] = a[0] + res[0];
        a[1] = a[1] + res[1];

        res = dfs(arr, next_level, x+next_level, y+next_level);
        a[0] = a[0] + res[0];
        a[1] = a[1] + res[1];
        return a;
    }

    public boolean check(int[][] arr, int level, int x, int y) {
        int target = arr[x][y];
        for (int i=0; i<level; i++) {
            for (int j=0; j<level; j++) {
                if (i == 0 && j == 0) {
                    continue;
                }
                if (target != arr[x+i][y+j]) {
                    return false;
                }
            }
        }
        return true;
    }
}