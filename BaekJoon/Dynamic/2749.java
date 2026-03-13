// === 원본 코드 ===
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// ctrl + alt + o -> 안쓰는 import 제거

// BeakJoon: 2749 - 피보나치 수 3
public class Main {

    private static long N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Long.parseLong(br.readLine());

        int period = 15 * 100000; // 피사노 주기 15 * 10 ^ (k - 1)

        long[] arr = new long[period];
        arr[1] = 1;
        for (int i = 2; i < period; i++) {
            arr[i] = (arr[i - 1] + arr[i - 2]) % 1_000_000;
        }

        System.out.println(arr[(int) (N % period)]);
    }
}

// === 코드 리뷰 반영 ===
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// ctrl + alt + o -> 안쓰는 import 제거

// BeakJoon: 2749 - 피보나치 수 3
public class Main {

    private static final int MOD = 1_000_000;
    // 피사노 주기: F(n) mod 10^k는 주기 15 * 10^(k-1)로 반복
    // mod = 10^6 (k=6) -> 주기 = 15 * 10^5 = 1,500,000
    private static final int PISANO_PERIOD = 15 * 100_000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long N = Long.parseLong(br.readLine());

        long[] fib = new long[PISANO_PERIOD];
        fib[1] = 1;
        for (int i = 2; i < PISANO_PERIOD; i++) {
            fib[i] = (fib[i - 1] + fib[i - 2]) % MOD;
        }

        System.out.println(fib[(int) (N % PISANO_PERIOD)]);
    }
}

/*
코드 리뷰 수정 사항:
- [높음] N을 불필요한 static 필드에서 main 메서드의 지역 변수로 변경
- [중간] 변수명 arr을 fib로 변경하여 피보나치 수열임을 명확히 표현
- [중간] 매직 넘버 100000을 100_000으로 포맷 일치
- [중간] MOD 상수(1_000_000)와 PISANO_PERIOD 상수 추출
- [제안] 피사노 주기에 대한 주석 보강

문제 접근 방법:
- 알고리즘 분류: 동적 계획법(Dynamic Programming), 수학(피사노 주기)
- 핵심 아이디어:
  * F(n) mod m은 주기적으로 반복되는 성질을 이용 (피사노 주기)
  * pi(10^k) = 15 * 10^(k-1) 공식 활용
  * mod = 10^6이므로 주기는 1,500,000
  * 배열에 한 주기분의 피보나치 수를 미리 계산 후 N % period로 조회
- 시간복잡도: O(1,500,000) - 배열 초기화
- 공간복잡도: O(1,500,000) - 약 12MB
- 경계 케이스: N=0, N=1 모두 정상 처리
*/
