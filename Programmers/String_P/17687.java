import java.util.*;

// 기존 코드
import java.util.*;

class Solution {
    public String solution(int n, int t, int m, int p) {
        String answer = "";
        String l = "";
        int cnt = 0;
        // true대신에 바로 아래에 있는 조건문으로 확인하도록 구현하는게 좋을듯 하다. 좀 더 직관적이고 코드도 짧아지니 좋다. 
        while (true) {
            if (l.length() >= t * m) {
                break;
            }
            l += Integer.toString(cnt, n);
            cnt++;
        }
        // p-1부터 시작해서 m씩 증가하기 때문에 p-1+m*step 이런식으로 구현가능하다.
        int idx = p-1;
        while (true) {
            if (answer.length() == t) {
                return answer.toUpperCase();
            }
            answer += l.charAt(idx);
            idx = idx + m;
        }
    }
}

// 좀 더 짧게 구현
class Solution {
    public String solution(int n, int t, int m, int p) {
        String answer = "";
        String l = "";
        int cnt = 0;
        while (l.length() < t*m) {
            l += Integer.toString(cnt++, n); // l에 문자열을 더하고나서 cnt값이 증가하게 된다.
        }
        for (int i=0; i<t; i++) {
            answer += l.charAt(p - 1 + i * m); // m만큼씩 인덱스가 뛴다. 
        }
        return answer.toUpperCase(); // 전부 대문자로 리턴하기.
    }
}