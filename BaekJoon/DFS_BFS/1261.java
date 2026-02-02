import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static int M;
    static int[] dx = new int[] {0, 0, 1, -1};
    static int[] dy = new int[] {1, -1, 0, 0};
    static int[][] visit;
    static String[] arr;

    static int bfs() {
        // 첫 번째 값을 기준으로 우선순위 큐 구현.
        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparing(a -> a[0]));
        q.add(new int[] {0, 0, 0}); // 벽 부순개수, 현재 위치
        visit[0][0] = 1;

        while (!q.isEmpty()) {
            int[] pos = q.poll();

            if (pos[1] == M - 1 && pos[2] == N - 1) {
                return pos[0];
            }

            for (int i = 0; i < 4; i++) {
                int nx = pos[1] + dx[i];
                int ny = pos[2] + dy[i];

                // 범위를 벗어나는 경우.
                if (nx < 0 || nx >= M || ny < 0 || ny >= N) {
                    continue;
                }

                // 다음 위치가 방문한 적이 있으면 패스.
                if (visit[nx][ny] > 0) {
                    continue;
                }

                // 다음 위치로 이동.
                visit[nx][ny] = 1;

                int w_count = pos[0] + ((arr[nx].charAt(ny) == '1') ? 1 : 0);
                q.add(new int[] {w_count, nx, ny});
            }
        }

        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new String[M];
        visit = new int[M][N];

        for (int i = 0; i < M; i++) {
            arr[i] = br.readLine();
        }

        System.out.println(bfs());
    }
}