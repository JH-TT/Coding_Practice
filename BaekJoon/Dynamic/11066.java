// === 원본 코드 ===
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// ctrl + alt + o -> 안쓰는 import 제거

// BeakJoon: 11066 - 파일 합치기
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        while (T-- > 0) {
            int K = Integer.parseInt(br.readLine());
            int[] files = new int[K + 1];
            int[] sum = new int[K + 1]; // 누적 합

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= K; i++) {
                files[i] = Integer.parseInt(st.nextToken());
                sum[i] = sum[i - 1] + files[i]; // 누적 합 계산
            }

            int[][] dp = new int[K + 1][K + 1];

            //길이별로 DP 테이블 채우기
            for (int len = 2; len <= K; len++) { // 길이 2부터 K까지
                for (int i = 1; i + len - 1 <= K; i++) { // 시작 위치
                    int j = i + len - 1; // 끝 위치
                    dp[i][j] = Integer.MAX_VALUE;

                    // k를 기준으로 [i, k]와 [k+1, j]로 분할
                    for (int k = i; k < j; k++) {
                        int cost = dp[i][k] + dp[k + 1][j] + (sum[j] - sum[i - 1]);
                        dp[i][j] = Math.min(dp[i][j], cost);
                    }
                }
            }

            sb.append(dp[1][K]).append('\n');
        }

        System.out.println(sb);
    }
}

// === 코드 리뷰 반영 ===
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// ctrl + alt + o -> 안쓰는 import 제거

// BeakJoon: 11066 - 파일 합치기
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        while (T-- > 0) {
            int K = Integer.parseInt(br.readLine());
            int[] sum = new int[K + 1]; // 누적 합

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= K; i++) {
                sum[i] = sum[i - 1] + Integer.parseInt(st.nextToken()); // 누적 합 계산
            }

            int[][] dp = new int[K + 1][K + 1];

            // 길이별로 DP 테이블 채우기
            for (int len = 2; len <= K; len++) { // 길이 2부터 K까지
                for (int i = 1; i + len - 1 <= K; i++) { // 시작 위치
                    int j = i + len - 1; // 끝 위치
                    dp[i][j] = Integer.MAX_VALUE;

                    // k를 기준으로 [i, k]와 [k+1, j]로 분할
                    for (int k = i; k < j; k++) {
                        int cost = dp[i][k] + dp[k + 1][j] + (sum[j] - sum[i - 1]);
                        dp[i][j] = Math.min(dp[i][j], cost);
                    }
                }
            }

            sb.append(dp[1][K]).append('\n');
        }

        System.out.print(sb);
    }
}

/*
코드 리뷰 수정 사항:
1. 불필요한 files 배열 제거 - 누적합 계산 후 다시 사용되지 않음
2. System.out.println() → System.out.print()로 변경 - 불필요한 이중 개행 방지
3. 주석 스타일 통일 - "//길이별로" → "// 길이별로" (공백 추가)

문제 접근 방법:
- 알고리즘: 구간 DP (Dynamic Programming)
- 핵심 아이디어:
  * dp[i][j] = i번째부터 j번째 파일까지 합치는 최소 비용
  * 구간 [i, j]를 중간 지점 k로 분할하여 [i, k]와 [k+1, j]로 나누기
  * dp[i][j] = min(dp[i][k] + dp[k+1][j] + sum(i~j)) for all k
  * 작은 구간부터 계산 (bottom-up): 길이 1 → 2 → ... → n
- 최적화: 누적 합 배열을 사용하여 구간 합을 O(1)에 계산
- 시간복잡도: O(K^3) - K개 파일, 각 구간마다 K번 탐색
*/
