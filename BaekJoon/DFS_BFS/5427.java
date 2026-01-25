import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final String SPACE = " ";
    private static final String BLANK = "";
    private static int[][] visit;
    private static Queue<int[]> fire_q;
    private static Queue<int[]> sang_q;
    private static int w;
    private static int h;
    private static String[][] arr;

    private static final int[] dx = new int[]{-1, 1, 0, 0};
    private static final int[] dy = new int[]{0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        final int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            String line = br.readLine();
            w = Integer.parseInt(line.split(SPACE)[0]);
            h = Integer.parseInt(line.split(SPACE)[1]);
            fire_q = new LinkedList<>(); // (x, y) 좌표
            sang_q = new LinkedList<>();

            arr = new String[h][w];
            visit = new int[h][w];

            for (int j = 0; j < h; j++) {
                String[] li = br.readLine().split(BLANK);
                for (int k = 0; k < w; k++) {
                    arr[j][k] = li[k];

                    if (li[k].equals("*")) {
                        fire_q.add(new int[]{j, k});
                        visit[j][k] = 1;
                        continue;
                    }

                    if (li[k].equals("@")) {
                        sang_q.add(new int[]{j, k});
                        visit[j][k] = 1;
                    }
                }
            }

            // bfs 시작
            int ti = 1;
            int res;
            while (true) {
                res = bfs();

                if (res == -1 || res == 1) {
                    break;
                }

                ti++;
            }

            if (res == 1) {
                System.out.println(ti);
            }

            if (res == -1) {
                System.out.println("IMPOSSIBLE");
            }
        }
    }

    /**
     * BFS
     *
     * @param arr 지도
     * @param i   현재 x좌표
     * @param j   현재 y좌표
     */
    public static int bfs() {
        Queue<int[]> sub_fire_q = new LinkedList<>();
        Queue<int[]> sub_sang_q = new LinkedList<>();

        while (!fire_q.isEmpty()) {
            int[] now_f = fire_q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = now_f[0] + dx[i];
                int ny = now_f[1] + dy[i];

                if (nx < 0 || nx >= h || ny < 0 || ny >= w) {
                    continue;
                }

                if (arr[nx][ny].equals("#")) {
                    continue;
                }

                if (visit[nx][ny] > 0) {
                    continue;
                }

                visit[nx][ny] = 1;

                sub_fire_q.add(new int[]{nx, ny});
            }
        }
        fire_q = new LinkedList<>(sub_fire_q);

        // 상근이는 범위를 벗어나야 탈출임.
        while (!sang_q.isEmpty()) {
            int[] now_s = sang_q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = now_s[0] + dx[i];
                int ny = now_s[1] + dy[i];

                if (nx < 0 || nx >= h || ny < 0 || ny >= w) {
                    return 1;
                }

                if (arr[nx][ny].equals("#")) {
                    continue;
                }

                if (visit[nx][ny] > 0) {
                    continue;
                }

                visit[nx][ny] = 1;

                sub_sang_q.add(new int[]{nx, ny});
            }
        }
        sang_q = new LinkedList<>(sub_sang_q);

        if (sang_q.isEmpty()) {
            return -1;
        }

        return 0;
    }
}