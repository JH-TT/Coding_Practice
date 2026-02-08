import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// ctrl + alt + o -> 안쓰는 import 제거

// BeakJoon: 9205 - 맥주 마시면서 걸어가기
public class Main {

    static int T;
    static int N;
    static int[][] pos; // 0: 집, 1~N: 편의점, N+1: 페스티벌
    static boolean[] visit; // 방문여부

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            N = Integer.parseInt(br.readLine());
            pos = new int[N + 2][2];
            visit = new boolean[N + 2];

            for (int i = 0; i < N + 2; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                pos[i][0] = Integer.parseInt(st.nextToken());
                pos[i][1] = Integer.parseInt(st.nextToken());
            }

            // BFS로 집(0)에서 페스티벌(N+1)까지 도달 가능한지 판별
            Queue<Integer> q = new LinkedList<>();
            q.add(0);
            visit[0] = true;

            boolean check = false;
            while (!q.isEmpty()) {
                int nowIdx = q.poll();

                for (int i = 1; i < N + 2; i++) {
                    if (visit[i]) continue;

                    int dist = Math.abs(pos[nowIdx][0] - pos[i][0]) + Math.abs(pos[nowIdx][1] - pos[i][1]);

                    if (dist > 1000) continue;

                    visit[i] = true;

                    if (i == N + 1) {
                        check = true;
                        break;
                    }

                    q.add(i);
                }

                if (check) break;
            }

            sb.append(check ? "happy" : "sad");
            sb.append("\n");
        }

        System.out.print(sb);
    }
}
