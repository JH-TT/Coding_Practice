import java.util.*;

class Solution {
    public int solution(int m, int n, String[] board) {
        int answer = 0;
        String[][] board2 = new String[m][n];
        for (int i=0; i<m; i++) {
            board2[i] = board[i].split("");
        }
        while (true) {
            // 조건에 부합하는 블럭 전부 찾기
            Set<String> blocks = findBlocks(board2, m, n);
            if (blocks.size() == 0) {
                break;
            }
            // 블럭 없애는 로직
            for (String block : blocks) {
                String[] pos = block.split(" ");
                int x = Integer.parseInt(pos[0]);
                int y = Integer.parseInt(pos[1]);
                board2[x][y] = "!";
                answer++;
            }
            // 블럭 아래로 내리는 로직
            board2 = move(board2, m, n);
        }
        
        return answer;
    }
    
    public Set<String> findBlocks(String[][] b, int m, int n) {
        Set<String> idxs = new HashSet<>();
        
        for (int i=0; i<m-1;i++) {
            for (int j=0; j<n-1; j++) {
                if (b[i][j].equals("!")) {
                    continue;
                }
                Set<String> set = new HashSet<String>();
                set.add(b[i][j]);
                set.add(b[i][j+1]);
                set.add(b[i+1][j]);
                set.add(b[i+1][j+1]);
                // 4블럭이 전부 같으면 4블럭 좌표 저장
                if (set.size() == 1) {
                    String x = Integer.toString(i);
                    String y = Integer.toString(j);
                    String x_next = Integer.toString(i+1);
                    String y_next = Integer.toString(j+1);
                    idxs.add(x+" "+y);
                    idxs.add(x_next+" "+y);
                    idxs.add(x+" " +y_next);
                    idxs.add(x_next+" "+y_next);
                }
            }
        }
        return idxs;
    }
    
    public String[][] move(String[][] b, int m, int n) {
        int level = 0;
        while (level < n) {
            Queue<String> height = new LinkedList<>();
            for (int i=m-1; i>-1; i--) {
                if (!b[i][level].equals("!")) {
                    height.add(b[i][level]);
                }
            }
            for (int i=m-1; i>-1; i--) {
                if (height.peek() == null) {
                    b[i][level] = "!";
                    continue;
                }
                b[i][level] = height.poll();
            }
            level++;
        }
        return b;
    }
}

// 그냥 구현문제
// 기능 2가지
// 1. 조건에 부합하는 모든 블럭의 좌표를 set에 넣어서 중복없이 저장하기
// 2. 블럭을 없앤뒤, 아래로 전부 내리기

// 활용한 함수들?
// board내부에 String을 Array로 변경하기
// split 활용
// set활용
// line 46 ~ 49는 그냥 char로 변경하기를 했다가 아스키코드기준으로 바뀐다는것을 늦게 알아챔 그래서 toString으로 변경