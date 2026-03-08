import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

// ctrl + alt + o -> 안쓰는 import 제거

// BeakJoon: 19238 - 스타트 택시
public class Main {

    private static int[][] arr;
    private static int[][] pos; // 손님 위치
    private static HashMap<Integer, List<Integer>> end = new HashMap<>(); // 손님 도착 위치
    private static int comp; // 완료한 손님
    private static int N;
    private static int M;
    private static int OIL;

    // 백준의 위치
    private static int B_R;
    private static int B_C;

    private static int[] dx = new int[]{0, 0, -1, 1};
    private static int[] dy = new int[]{-1, 1, 0, 0};

    private static int human;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        OIL = Integer.parseInt(st.nextToken());

        arr = new int[N + 1][N + 1];
        pos = new int[N + 1][N + 1];
        comp = 0;

        for (int i = 1; i < N + 1; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j < N + 1; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        // 백준의 위치
        B_R = Integer.parseInt(st.nextToken());
        B_C = Integer.parseInt(st.nextToken());

        // 사람들의 시작위치, 도착위치
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int pr = Integer.parseInt(st.nextToken()); // 손님 행
            int pc = Integer.parseInt(st.nextToken()); // 손님 열
            int gr = Integer.parseInt(st.nextToken()); // 손님 도착 행
            int gc = Integer.parseInt(st.nextToken()); // 손님 도착 열

            pos[pr][pc] = i + 1;
            end.put(i + 1, List.of(gr, gc));
        }

        // 손님을 더 이상 태울 수 없는 경우. -1
        while (true) {
            boolean res = human_bfs(); // 사람태우기.
            if (!res || OIL <= 0) {
                System.out.println(-1);
                break;
            }

            res = goal_bfs(); // 도착지로 이동
            if (res) {
                comp++;

                // 모든 손님을 이동시켰다면.
                if (comp == M) {
                    System.out.println(OIL);
                    break;
                }
            } else {
                System.out.println(-1);
                break;
            }
        }
    }

    // 손님이면 손님번호, 도착이면 이동거리를 리턴한다.
    private static boolean human_bfs() {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
            return Integer.compare(a[2], b[2]);
        });
        pq.add(new int[]{0, B_R, B_C});

        int[][] visit = new int[N + 1][N + 1];
        visit[B_R][B_C] = 1;

        while (!pq.isEmpty()) {
            int[] info = pq.poll();

            if (pos[info[1]][info[2]] > 0) {
                OIL -= info[0];
                // 백준 위치 조정.
                B_R = info[1];
                B_C = info[2];

                human = pos[info[1]][info[2]];
                pos[info[1]][info[2]] = 0;

                return true;
            }

            // 최솟값이 OIL 연료를 넘으면 실패.
            if (OIL <= info[0]) {
                continue;
            }

            for (int i = 0; i < 4; i++) {
                int nx = info[1] + dx[i];
                int ny = info[2] + dy[i];

                if (nx < 1 || nx > N || ny < 1 || ny > N) {
                    continue;
                }

                if (arr[nx][ny] == 1) {
                    continue;
                }

                if (visit[nx][ny] == 1) {
                    continue;
                }

                visit[nx][ny] = 1;
                pq.add(new int[]{info[0] + 1, nx, ny});
            }
        }

        return false;
    }

    private static boolean goal_bfs() {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
            return Integer.compare(a[2], b[2]);
        });
        pq.add(new int[]{0, B_R, B_C});

        int[][] visit = new int[N + 1][N + 1];
        visit[B_R][B_C] = 1;

        while (!pq.isEmpty()) {
            int[] info = pq.poll();

            List<Integer> g = end.get(human);
            if (g.get(0) == info[1] && g.get(1) == info[2]) {
                OIL += info[0];

                // 백준 위치 조정.
                B_R = info[1];
                B_C = info[2];

                return true;
            }

            if (OIL <= info[0]) {
                continue;
            }

            for (int i = 0; i < 4; i++) {
                int nx = info[1] + dx[i];
                int ny = info[2] + dy[i];

                if (nx < 1 || nx > N || ny < 1 || ny > N) {
                    continue;
                }

                if (arr[nx][ny] == 1) {
                    continue;
                }

                if (visit[nx][ny] == 1) {
                    continue;
                }

                visit[nx][ny] = 1;
                pq.add(new int[]{info[0] + 1, nx, ny});
            }
        }

        return false;
    }
}
