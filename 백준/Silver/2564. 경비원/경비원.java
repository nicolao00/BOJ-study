import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

// 40 / 721
public class Main {
    static int width, height;
    static int N;
    static int[][] stores;
    static int[] start;


    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        width = Integer.parseInt(st.nextToken());
        height = Integer.parseInt(st.nextToken());

        N = Integer.parseInt(bf.readLine());

        stores = new int[N][2];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(bf.readLine());
            stores[i][0] = Integer.parseInt(st.nextToken());
            stores[i][1] = Integer.parseInt(st.nextToken());
        }

        start = new int[2];
        st = new StringTokenizer(bf.readLine());
        start[0] = Integer.parseInt(st.nextToken());
        start[1] = Integer.parseInt(st.nextToken());

        int answer = 0;
        for (int i = 0; i < N; i++) {
            // 시작 점이 북 1 or 남 2
            if (start[0] == 1 || start[0] == 2) {
                // 가게가 북 1 or 남 2
                if (stores[i][0] == 1 || stores[i][0] == 2) {
                    if (stores[i][0] == start[0])
                        answer += Math.abs(stores[i][1] - start[1]);
                    else
                        answer += Math.min(width - stores[i][1] + width - start[1], stores[i][1] + start[1]) + height;
                }
                // 가게가 서 3, 동 4
                else {
                    if (stores[i][0] == 3)
                        answer += start[1];
                    else
                        answer += width - start[1];
                    if (start[0] == 1)
                        answer += stores[i][1];
                    else
                        answer += height - stores[i][1];
                }
            }
            // 시작 점이 서 3, 동 4
            else {
                // 가게가 서 3, 동 4
                if (stores[i][0] == 3 || stores[i][0] == 4) {
                    if (stores[i][0] == start[0])
                        answer += Math.abs(stores[i][1] - start[1]);
                    else
                        answer += Math.min(height - stores[i][1] + height - start[1], stores[i][1] + start[1]) + width;
                }
                // 가게가 북1 or 남2
                else {
                    if (stores[i][0] == 1)
                        answer += start[1];
                    else
                        answer += height - start[1];
                    if (start[0] == 3)
                        answer += stores[i][1];
                    else
                        answer += width - stores[i][1];
                }
            }
        }
        System.out.println(answer);
    }
}