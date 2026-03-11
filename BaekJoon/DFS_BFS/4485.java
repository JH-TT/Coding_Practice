// === 원본 코드 ===
/*
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// ctrl + alt + o -> 안쓰는 import 제거

// BeakJoon: 4485 - 녹색 옷 입은 애가 젤다지?
public class Main {

    private static int[][] arr;
    private static int[][] visit;   // visit[x][y] (x, y)위치에 있을 때 잃는 최소 루피

    private final static int[] dx = {0, 0, -1, 1};
    private final static int[] dy = {1, -1, 0, 0};

    private static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();

        int p = 1;
        while (true) {
            N = Integer.parseInt(br.readLine());

            if (N == 0) break;

            arr = new int[N][N];
            visit = new int[N][N];

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
                Arrays.fill(visit[i], Integer.MAX_VALUE);
            }

            int res = bfs();

            sb.append("Problem ").append(p++).append(": ").append(res);
            sb.append("\n");
        }

        System.out.println(sb);
    }

    public static int bfs() {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {0, 0});
        visit[0][0] = arr[0][0];

        while (!q.isEmpty()) {
            int[] pos = q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = pos[0] + dx[i];
                int ny = pos[1] + dy[i];

                if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                    continue;
                }

                int rupee = visit[pos[0]][pos[1]] + arr[nx][ny];

                // 현재 경로가 루피가 더 소비되면 스킵
                if (visit[nx][ny] <= rupee) {
                    continue;
                }

                visit[nx][ny] = rupee;

                q.add(new int[]{nx, ny});
            }
        }

        return visit[N - 1][N - 1];
    }
}
*/

// === 코드 리뷰 반영 ===
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

// ctrl + alt + o -> 안쓰는 import 제거

// BeakJoon: 4485 - 녹색 옷 입은 애가 젤다지?
public class Main {

    private static final int[] dx = {0, 0, -1, 1};
    private static final int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int p = 1;
        int N;
        while ((N = Integer.parseInt(br.readLine().trim())) != 0) {
            int[][] arr = new int[N][N];
            int[][] dist = new int[N][N];

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
                Arrays.fill(dist[i], Integer.MAX_VALUE);
            }

            int result = dijkstra(arr, dist, N);
            sb.append("Problem ").append(p++).append(": ").append(result).append("\n");
        }

        System.out.print(sb);
    }

    private static int dijkstra(int[][] arr, int[][] dist, int N) {
        // {비용, x, y} - 비용 기준 오름차순 정렬
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        dist[0][0] = arr[0][0];
        pq.offer(new int[]{arr[0][0], 0, 0});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int cost = cur[0], x = cur[1], y = cur[2];

            // 이미 더 좋은 경로로 확정된 노드는 스킵
            if (cost > dist[x][y]) continue;

            // 도착점 도달 시 즉시 반환 (최적화)
            if (x == N - 1 && y == N - 1) return cost;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;

                int newCost = cost + arr[nx][ny];
                if (newCost < dist[nx][ny]) {
                    dist[nx][ny] = newCost;
                    pq.offer(new int[]{newCost, nx, ny});
                }
            }
        }

        return dist[N - 1][N - 1];
    }
}

/*
코드 리뷰 수정 사항:
- 일반 Queue 대신 PriorityQueue를 사용한 다익스트라 알고리즘 적용
  (시간 복잡도 O(N^4) → O(N^2 log N)으로 개선)
- LinkedList 대신 PriorityQueue 사용
- 변수명 개선: visit → dist (의미가 더 명확)
- 메서드명 개선: bfs() → dijkstra()
- 중복 노드 처리: cost > dist[x][y] 체크 추가
- 조기 종료: 도착점 도달 시 즉시 반환
- static 필드를 지역 변수로 변경하여 메서드 매개변수로 전달
- 출력 개선: println → print (불필요한 빈 줄 제거)

문제 접근 방법:
- 알고리즘 분류: 다익스트라 (최단 경로)
- 핵심 아이디어:
  * N x N 격자에서 (0,0)에서 (N-1,N-1)까지 이동할 때 잃는 루피의 최솟값 구하기
  * 가중치가 있는 그래프의 최단 경로 문제이므로 다익스트라 알고리즘 사용
  * PriorityQueue를 사용하여 현재까지의 최소 비용을 기준으로 탐색
  * dist 배열로 각 위치까지의 최소 비용을 저장하고 갱신
- 시간복잡도: O(N^2 log N) (N ≤ 125)
*/
