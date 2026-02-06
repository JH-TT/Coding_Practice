import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// ctrl + alt + o -> 안쓰는 import 제거

// BeakJoon: 2343 - 기타레슨
public class Main {
    static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // M개의 그룹을 만들었을 때, 최소... -> 이분탐색
        // 이분탐색을 하면서 M개의 그룹이 만들어지는지 보고 M개이하의 그룹이 만들어지면 true, 아니면 false로 가면서 최적의 답에 접근한다. (upper bound)
        int start = -1;
        int end = Arrays.stream(arr).sum();

        while (start + 1 < end) {
            int mid = (start + end) / 2;
            if (test(arr, mid)) {
                end = mid;
            } else {
                start = mid;
            }
        }

        System.out.println(end);
    }

    public static boolean test(int[] arr, int size) {
        int cnt = 1; // 블루레이 그룹 개수
        int total = 0; // 현재 그룹의 총 강의길이

        for (int i : arr) {
            if (i > size) {
                return false;
            }

            // 다른 그룹 추가
            if (total + i > size) {
                total = i;
                cnt++;
                continue;
            }

            // 현재 그룹에 추가
            total += i;
        }

        return cnt <= M;
    }
}
