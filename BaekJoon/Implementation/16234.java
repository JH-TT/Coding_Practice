import java.io.*;
import java.util.*;

class Main {

    private static final int[] dx = new int[]{-1, 1, 0, 0};
    private static final int[] dy = new int[]{0, 0, -1, 1};
    private static int[][] arr;
    private static int n;
    private static int r;
    private static int l;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        n = Integer.parseInt(input.split(" ")[0]);
        l = Integer.parseInt(input.split(" ")[1]);
        r = Integer.parseInt(input.split(" ")[2]);
        arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(line[j]);
            }
        }
        int res = 0;
        while(true) {
            int[][] visit = new int[n][n];
            if(start(visit)){
                res++;
                continue;
            }
            break;
        }
        System.out.println(res);
    }

    public static void printState(int[][] visit) {
        for (int i = 0; i < n; i++) {
            System.out.println(Arrays.toString(visit[i]));
        }
        System.out.println();
    }
    public static boolean start(int[][] visit) {
        boolean flag = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(visit[i][j] == 1) {
                    continue;
                }
                if(bfs(i, j, visit)){
                    flag = true;
                }
            }
        }
        return flag;
    }

    public static boolean bfs(int x, int y, int[][] visit) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});
        visit[x][y] = 1;
        boolean flag = false;
        List<int[]> a = new ArrayList<>();
        a.add(new int[]{x, y, arr[x][y]});
        while(!q.isEmpty()) {
            int[] now = q.poll(); // x, y, total, cnt
            for (int i = 0; i < 4; i++) {
                int nx = now[0] + dx[i];
                int ny = now[1] + dy[i];
                if(nx < 0 || nx >= n || ny < 0 || ny >= n) {
                    continue;
                }
                if(visit[nx][ny] == 0) {
                    int diff = Math.abs(arr[now[0]][now[1]] - arr[nx][ny]);
                    if(!(l <= diff && diff <= r)) {
                        continue;
                    }
                    visit[nx][ny] = 1;
                    flag = true;
                    a.add(new int[]{nx, ny, arr[nx][ny]});
                    q.add(new int[]{nx, ny});
                }
            }
        }
        change(a);
        return flag;
    }

    public static void change(List<int[]> a) {
        Integer total = a.stream().map(x -> x[2]).reduce(0, Integer::sum);
        int mean = total / a.size();
        for(int[] cor : a) {
            arr[cor[0]][cor[1]] = mean;
        }
    }
}

// 구현 + bfs 문제.