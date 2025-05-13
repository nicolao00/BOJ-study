// 201
import java.util.*;
import java.io.*;

class Main {
    static int N, K;
    static int[][] medals;
    static int[] target;

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        medals = new int[N+1][3];
        target = new int[3];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(bf.readLine());
            int countryNum = Integer.parseInt(st.nextToken());
            for (int mIdx = 0; mIdx < 3; mIdx++) {
                medals[countryNum][mIdx] = Integer.parseInt(st.nextToken());
            }
        }

        target = medals[K];
        Arrays.sort(medals, (o1, o2) -> {
            if (o1[0] == o2[0]) {
                if (o1[1] == o2[1]) {
                    return o2[2] - o1[2];
                } else {
                    return o2[1] - o1[1];
                }
            } else {
                return o2[0] - o1[0];
            }
        });

        int answer = 0;
        for (int i = 0; i < N; i++) {
            if (medals[i][0] > target[0]) {
                answer += 1;
            } else if (medals[i][0] == target[0]) {
                if (medals[i][1] > target[1]) {
                    answer += 1;
                } else if (medals[i][1] == target[1]) {
                    if (medals[i][2] > target[2]) {
                        answer += 1;
                    }
                    else {
                        System.out.println(answer+1);
                        break;
                    }
                } else {
                    System.out.println(answer+1);
                    break;
                }
            } else {
                System.out.println(answer+1);
                break;
            }
        }
    }
}