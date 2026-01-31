import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.TreeSet;

public class Main {

    static int gcd(int a, int b) {
        int max = Math.max(a, b);
        int min = Math.min(a, b);

        if (max % min == 0) {
            return min;
        }

        return gcd(min, max % min);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        int[] diff = new int[N - 1];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int[] sortedArr = Arrays.stream(arr).sorted().toArray();
        // 차이를 구한다.
        for (int i = 0; i < N - 1; i++) {
            diff[i] = sortedArr[i + 1] - sortedArr[i];
        }

        int gcd = diff[0];

        // 배열diff에서 최대공약수를 구한다.
        for (int i = 1; i < diff.length; i++) {
            gcd = gcd(gcd, diff[i]);
        }

        // gcd의 약수를 구하자 (단, 1보다 큰 약수만 구하고 중복은 X -> TreeSet)
        TreeSet<Integer> set = new TreeSet<>();
        for (int i = 2; i <= ((int) Math.sqrt(gcd)) + 1; i++) {
            if (gcd % i == 0) {
                set.add(i);
                if (i != gcd / i) {
                    set.add(gcd / i);
                }
            }
        }

        if (gcd / 2 + 1 != gcd) {
            set.add(gcd);
        }

        for (Integer i : set) {
            System.out.print(i + " ");
        }
    }
}