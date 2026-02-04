import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        int[][] arr = new int[19][19];

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력
        for (int i = 0; i < 19; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 19; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 결과가 났는지 확인한다.
        // 우로 5개, 아래로 5개, 오른쪽 아래 대각선, 오른쪽 위 대각선 으로 5개 이렇게 4방향만 확인한다.
        // ㄴ 이유는 애초에 문제에서 "이긴 돌이 있으면 가장 위에 있는 것의 좌표를 출력"하라는거 보면 이거 유도한듯함.

        // 결과
        boolean check = false;

        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 19; j++) {
                // 더 이상 오목이 될 수 없는 좌표면 종료한다.
                if (i > 14 && j > 14) break;
                // 아무 돌이 없으면 스킵
                if (arr[i][j] == 0) continue;

                // 가로 (1번 세로줄 기준이거나, 현재 위치기준 왼쪽에 돌이 없어야 함)
                if (j == 0 || arr[i][j] != arr[i][j - 1]) {
                    for (int k = 1; k < 6; k++) {
                        if (k == 5) {
                            // 만약 6개이상 놓였다면 실패
                            if (j + k < 19 && arr[i][j] == arr[i][j + k]) {
                                break;
                            }
                            check = true;
                            System.out.println(arr[i][j]);
                            System.out.println((i + 1) + " " + (j + 1));
                            break;
                        }

                        // 범위를 벗어나면 실패
                        if (j + k >= 19) {
                            break;
                        }

                        // 다른 돌 또는 비어있으면 실패
                        if (arr[i][j] != arr[i][j + k]) {
                            break;
                        }
                    }
                }

                if (check) {
                    break;
                }

                // 세로 (1번 라인을 보고있거나, 위에 같은 색의 돌이 없어야 함)
                if (i == 0 || (arr[i][j] != arr[i - 1][j])) {
                    for (int k = 1; k < 6; k++) {
                        if (k == 5) {
                            if (i + k < 19 && arr[i][j] == arr[i + k][j]) {
                                break;
                            }
                            check = true;
                            System.out.println(arr[i][j]);
                            System.out.println((i + 1) + " " + (j + 1));
                            break;
                        }

                        if (i + k >= 19) {
                            break;
                        }

                        if (arr[i][j] != arr[i + k][j]) {
                            break;
                        }
                    }
                }

                if (check) {
                    break;
                }

                // 대각선 (오른쪽 아래)
                if (i == 0 || j == 0 || arr[i][j] != arr[i - 1][j - 1]) {
                    for (int k = 0; k < 6; k++) {
                        if (k == 5) {
                            if (i + k < 19 && j + k < 19 && arr[i][j] == arr[i + k][j + k]) {
                                break;
                            }
                            check = true;
                            System.out.println(arr[i][j]);
                            System.out.println((i + 1) + " " + (j + 1));
                            break;
                        }

                        if (i + k >= 19 || j + k >= 19) {
                            break;
                        }

                        if (arr[i][j] != arr[i + k][j + k]) {
                            break;
                        }
                    }
                }

                // 대각선 (오른쪽 위)
                if (i == 18 || j == 0 || arr[i][j] != arr[i + 1][j - 1]) {
                    for (int k = 0; k < 6; k++) {
                        if (k == 5) {
                            if (i - k >= 0 && j + k < 19 && arr[i][j] == arr[i - k][j + k]) {
                                break;
                            }
                            check = true;
                            System.out.println(arr[i][j]);
                            System.out.println((i + 1) + " " + (j + 1));
                            break;
                        }

                        if (i - k < 0 || j + k >= 19) {
                            break;
                        }

                        if (arr[i][j] != arr[i - k][j + k]) {
                            break;
                        }
                    }
                }

                if (check) {
                    break;
                }
            }

            if (check) {
                break;
            }
        }

        // 아무런 승부가 결정되지 않았다면...
        if (!check) {
            System.out.println(0);
        }
    }
}

// 간단한 구현문제긴 한데...
// 조건문 처리가 잘못하면 그냥 넘겨버릴 경우가 있었다.