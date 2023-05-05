import java.util.*;

class Solution {
    public int[] solution(String msg) {
        List<Integer> answer = new ArrayList<>();
        HashMap<String, Integer> d = new HashMap<>();
        // 해시맵에 A-Z까지 미리 넣기
        for (int i=1; i<27; i++) {
            d.put(Character.toString((char) 64+i), i);
        }
        Integer idx = 27;
        String word = "";
        for (int i=0; i<msg.length(); i++) {
            char m = msg.charAt(i);
            if (!d.containsKey(word + m)) {
                answer.add(d.get(word));
                d.put(word+m, idx++);
                word = "";
            }
            word = word + m;
        }
        answer.add(d.get(word));
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}

// 해시맵을 사용하는것
// 아스키코드를 이용하는것
// ArrayList에서 Array로 변환하는것 + stream의 사용 