import java.util.*;

class Solution {
    public String[] solution(String[] files) {
        String[] answer = {};
        Stack<String> res = new Stack<>();
        HashMap<String, String> head = new HashMap<>();
        HashMap<String, Integer> number = new HashMap<>();
        // head, number구하기
        for (String file : files) {
            String h = "";
            String num = "";
            int i = 0;
            
            while (!Character.isDigit(file.charAt(i)) && i < file.length()) {
                h = h + file.charAt(i++);
            }
            // 조건문 순서 주의! i가 맞는 범위인지 확인한 다음 charAt을 확인하도록 구현
            while (i < file.length() && Character.isDigit(file.charAt(i)) && num.length() <= 5) {
                num = num + file.charAt(i++);
            }
            head.put(file, h.toLowerCase()); // 대소문자는 구분하지 않으니 해시맵에는 소문자로 통일한다.
            number.put(file, Integer.parseInt(num));
        }
        // 정렬 시작
        for (String file : files) {
            if (res.empty()) {
                res.push(file);
                continue;
            }
            // 하나씩 비교
            Stack<String> sub = new Stack<>();
            while (!res.empty()) {
                String a = res.peek(); // 맨 위에를 꺼냄
                // file이 a보다 앞서는지 확인한다. 
                // file이 앞서면 a는 따로 빼놓고 다음 파일 확인
                if (check(a, file, head, number)) {
                    sub.push(res.pop());
                } else { // 아니면 바로 푸쉬한다.
                    res.push(file);
                    break;
                }
            }
            // while문을 나왔는데 res가 그대로 비어있다는건 file이 제일 앞이라는 소리.
            if (res.empty()) {
                res.push(file);
            }
            // sub에 있는 파일을 다시 옮긴다.
            while (!sub.empty()) {
                res.push(sub.pop());
            }
        }
        return res.toArray(new String[res.size()]);
    }
    // 두 파일 비교하기 a가 타겟, b가 주체
    public boolean check(String a, String b, HashMap h, HashMap n) {
        // head먼저 비교하기
        String a_head = (String) h.get(a);
        String b_head = (String) h.get(b);
        // 타겟이 사전순으로 앞이면 주체는 a보다 뒤에 있어야 한다. 그러니 false
        int r = a_head.compareTo(b_head);
        if (r < 0) {
            return false;
        } else if (r > 0) {
            return true;
        } else {
            // head가 같으면 number를 비교한다.
            // b가 먼저면 true, 아니면 false
            Integer a_num = (Integer) n.get(a);
            Integer b_num = (Integer) n.get(b);
            int rr = a_num.compareTo(b_num);
            // 음수면 b가 더 작음, a와 같으면 그냥 순서대로 저장.
            if (rr <  0 || rr == 0) {
                return false;
            }
            return true;
        }
    }
}


// 다른 사람 풀이
import java.util.*;
import java.util.regex.*;

class Solution {
    public String[] solution(String[] files) {
        Pattern p = Pattern.compile("([a-z\\s.-]+)([0-9]{1,5})");

        Arrays.sort(files, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                Matcher m1 = p.matcher(s1.toLowerCase());
                Matcher m2 = p.matcher(s2.toLowerCase());
                m1.find();
                m2.find();

                if(!m1.group(1).equals(m2.group(1))) {
                    return m1.group(1).compareTo(m2.group(1));
                } else {
                    return Integer.parseInt(m1.group(2)) - Integer.parseInt(m2.group(2));
                }
            }
        });

        return files;
    }
}
// 정렬 함수에 비교함수를 넣어서 정렬함.