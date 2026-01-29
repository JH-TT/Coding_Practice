import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static int res = Integer.MAX_VALUE; // 결과값
    static int[][] arr;
    static int[][] visit;       // 실제 로직에 사용할 visit
    static int[][] visit2;      // 섬 그룹지을때 사용할 방문체크용 visit
    static int[] dx = new int[] {1, -1, 0, 0};
    static int[] dy = new int[] {0, 0, 1, -1};

    /**
     * 섬 그룹 초기화를 위한 bfs
     * @param island_no
     * @param x
     * @param y
     */
    public static void bfs(int island_no, int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});

        visit2[x][y] = 1;
        arr[x][y] = island_no;

        while (!q.isEmpty()) {
            int[] pos = q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = pos[0] + dx[i];
                int ny = pos[1] + dy[i];

                if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                    continue;
                }

                if (arr[nx][ny] == 0 || visit2[nx][ny] == 1) {
                    continue;
                }

                visit2[nx][ny] = 1;
                arr[nx][ny] = island_no;
                q.add(new int[]{nx, ny});
            }
        }
    }

    /**
     * 실제로직 bfs. </br>
     * 현재 최소 다리개수 정보를 가진 visit을 보면서 업데이트 한다.
     * @param x
     * @param y
     */
    public static void bfs2(int x, int y) {
        int island_no = arr[x][y]; // 섬 그룹 번호.

        visit[x][y] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.add(new int[]{0, x, y});

        while (!pq.isEmpty()) {
            int[] info = pq.poll();
            boolean quit = false;

            for (int i = 0; i < 4; i++) {
                int nx = info[1] + dx[i];
                int ny = info[2] + dy[i];

                if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                    continue;
                }

                // 다른 섬 만남!
                if (arr[nx][ny] > 0 && arr[nx][ny] != island_no) {
                    res = Math.min(res, info[0]);
                    quit = true;
                    break;
                }

                // 위 조건문을 통과했다는건 같은 섬을 만난 경우.
                if (arr[nx][ny] > 0) {
                    continue;
                }

                // 다음 위치의 최소다리 개수가 이미 현재 다리개수 + 1보다 같거나 적으면 스킵.
                if (visit[nx][ny] <= info[0] + 1) {
                    continue;
                }

                // 최소다리 업데이트
                visit[nx][ny] = info[0] + 1;
                pq.add(new int[]{info[0] + 1, nx, ny});
            }

            if (quit) break;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];
        visit = new int[N][N];
        visit2 = new int[N][N];

        /**
         * 초기화. arr과 visit을 초기화 한다.
         */
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
            Arrays.fill(visit[i], Integer.MAX_VALUE);
        }

        /**
         * bfs를 사용해서 각 섬의 그룹을 정한다.
         */
        int island_no = 1;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == 0 || visit2[i][j] == 1) {
                    continue;
                }

                bfs(island_no++, i, j);
            }
        }

        /**
         * bfs를 돈다.
         */
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == 0) {
                    continue;
                }

                // 사방이 육지인지 판단하는 변수.
                boolean land = true;
                for (int k = 0; k < 4; k++) {
                    int nx = i + dx[k];
                    int ny = j + dy[k];

                    if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                        continue;
                    }

                    if (arr[nx][ny] == 0) {
                        land = false;
                        break;
                    }
                }

                if (land) continue;

                bfs2(i, j);
            }
        }

        System.out.println(res);
    }
}

/**
 * 풀이
 *
 * 각 섬에 대해 라벨링을 bfs로 진행한다.
 * 그런 다음 각 섬의 가장자리만 bfs를 돌려서 다른 섬까지 최소거리를 구한다.
 */