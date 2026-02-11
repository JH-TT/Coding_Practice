import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

// BeakJoon: 1914 - 하노이 탑
public class Main {

    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        BigInteger moveCnt = BigInteger.TWO.pow(N).subtract(BigInteger.ONE);
        System.out.println(moveCnt);

        if (N <= 20) {
            dfs(N, 1, 3);
            System.out.print(sb);
        }
    }

    public static void dfs(int n, int from, int to) {
        if (n == 1) {
            sb.append(from).append(" ").append(to).append("\n");
            return;
        }
        int via = 6 - from - to;
        dfs(n - 1, from, via);
        sb.append(from).append(" ").append(to).append("\n");
        dfs(n - 1, via, to);
    }
}
