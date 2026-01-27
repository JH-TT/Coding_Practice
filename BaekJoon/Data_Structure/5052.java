import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());

            HashMap<String, Integer> dict = new HashMap<>();

            boolean flag = false;
            for (int j = 0; j < N; j++) {
                st = new StringTokenizer(br.readLine());

                String key = st.nextToken();
                if (dict.containsKey(key)) {
                    flag = true;
                    System.out.println("NO");
                    break;
                }

                dict.put(key, 1);
            }

            // 이미 결과가 나왔으면 스킵
            if (flag) {
                continue;
            }

            for (String s : dict.keySet()) {
                StringBuilder sb = new StringBuilder();
                flag = false;
                for (int j = 0; j < s.length(); j++) {
                    sb.append(s.charAt(j));

                    if (j != s.length() - 1 && dict.containsKey(sb.toString())) {
                        System.out.println("NO");
                        flag = true;
                        break;
                    }
                }

                if (flag) {
                    break;
                }
            }

            if (!flag) {
                System.out.println("YES");
            }
        }
    }
}


// 추가풀이 - 트라이
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Main {

    static class TrieNode {
        TrieNode[] children = new TrieNode[10]; // 0-9 숫자
        boolean endOfWord = false;

        boolean hasChildren() {
            for (TrieNode child : children) {
                if (child != null) return true;
            }
            return false;
        }
    }

    static class Trie {
        TrieNode root = new TrieNode();

        boolean insert(String number) {
            TrieNode node = root;

            for (int i = 0; i < number.length(); i++) {
                int idx = number.charAt(i) - '0';

                if (node.children[idx] == null) {
                    node.children[idx] = new TrieNode();
                }
                node = node.children[idx];

                //1. 이미 삽입된 번호가 현재 번호의 접두어
                if (node.endOfWord) {
                    return false;
                }
            }

            //2. 현재 번호가 이미 삽입된 번호의 접두어
            if (node.hasChildren()) {
                return false;
            }

            node.endOfWord = true;
            return true;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            int n = Integer.parseInt(br.readLine());
            String[] numbers = new String[n];

            for (int i = 0; i < n; i++) {
                numbers[i] = br.readLine();
            }

            // 짧은 번호부터 삽입해야 정확히 판별 가능
            Arrays.sort(numbers, Comparator.comparing(String::length));

            Trie trie = new Trie();
            boolean consistent = true;

            for (String number : numbers) {
                if (!trie.insert(number)) {
                    consistent = false;
                    break;
                }
            }

            sb.append(consistent ? "YES" : "NO").append("\n");
        }

        System.out.println(sb);
    }
}

/*
        ## 핵심 포인트

| 구분 | 설명 |
|------|------|
| **정렬 이유** | 짧은 번호를 먼저 삽입해야 "짧은 게 긴 것의 접두어" 케이스를 확실히 잡음 |
| **Case 1** | 삽입 도중 `endOfWord=true`인 노드 → 기존 번호가 접두어 |
| **Case 2** | 삽입 완료 후 자식이 존재 → 현재 번호가 기존 번호의 접두어 |
| **시간복잡도** | O(N × L) — N은 전화번호 개수, L은 최대 길이 |

## 동작 예시

입력: ["911", "97625999", "91125426"]

        1. 정렬 후: ["911", "91125426", "97625999"]

        2. "911" 삽입 → 성공, endOfWord 표시

3. "91125426" 삽입 시
   → 9 → 1 → 1 (여기서 endOfWord=true 발견!)
        → "911"이 "91125426"의 접두어 → NO
 */


// 추가풀이 2 - 정렬
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            int n = Integer.parseInt(br.readLine());
            String[] numbers = new String[n];

            for (int i = 0; i < n; i++) {
                numbers[i] = br.readLine();
            }

            // 사전순 정렬
            Arrays.sort(numbers);

            boolean consistent = true;

            for (int i = 0; i < n - 1; i++) {
                if (numbers[i + 1].startsWith(numbers[i])) {
                    consistent = false;
                    break;
                }
            }

            sb.append(consistent ? "YES" : "NO").append("\n");
        }

        System.out.println(sb);
    }
}

// 사전순으로 정렬한 뒤에 인접한 값끼리 startsWith를 사용해서 접두어인지 확인만 하면 된다.