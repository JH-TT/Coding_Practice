import java.util.*;

class Solution {
    public int solution(String dirs) {
        int answer = 0;
        char[] d = dirs.toCharArray();
        int[] pos = {0, 0};
        Set<String> visit = new HashSet();
        for (char a : d) {
            int[] next = pos.clone();
            if (a == 'U') {
                if (pos[1] < 5) {
                    next[1]++;
                }
            } else if (a == 'D') {
                if (pos[1] > -5) {
                    next[1]--;
                }
            } else if (a == 'R') {
                if (pos[0] < 5) {
                    next[0]++;
                }
            } else {
                if (pos[0] > -5) {
                    next[0]--;
                }
            }
            String str = Arrays.toString(pos);
            String posStr = str.substring(1, str.length()-1).replace(", ", "");
            String str2 = Arrays.toString(next);
            String nextStr = str2.substring(1, str2.length()-1).replace(", ", "");
            if (posStr.equals(nextStr)) {
                continue;
            }
            visit.add(posStr+" "+nextStr);
            visit.add(nextStr+" "+posStr);
            pos = next;
        }
        
        return visit.size()/2;
    }
}

# 아주 중요한 부분!!
# 이 문제는 처음 가는 "길"의 개수를 묻는거지 처음 가는 좌표를 묻는 문제가 아님
# 이 차이는 "RLRL"이라는 테케를 보면 전자기준으로는 0, 0 에서 0, 1로 가는 길만 왔다갔다 했기 때문에 답이 1이지만
# 후자는 좌표자체는 2개만 왔다갔다 했기 때문에 답이 2가된다.
# 이 차이를 생각하고 문제를 풀었어야 했다.