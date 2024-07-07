import java.util.*;
import java.io.*;

class Main {
    static int N;
    static int[][] playerEninig;
    static int[] lineUp = new int[9];
    static int answer;
    static boolean[] visit = new boolean[9];

    public static void makeSeq(int cnt) {
        if (cnt == 9) {
            dfs(0, 0, 0);
            return;
        }
        if (cnt == 3) {  // 1번 타자를 4번 자리에 고정
            lineUp[cnt] = 0;
            makeSeq(cnt+1);
            return;
        }

        for(int i = 1; i < 9; i++){
            if (!visit[i]){
                visit[i] = true;
                lineUp[cnt] = i;
                makeSeq(cnt+1);
                visit[i] = false;
            }
        }
    }

    public static void dfs(int eIdx, int result, int endPIdx) {
        if (eIdx == N){
            answer = Math.max(result, answer);
            return;
        }

        int outs = 0;
        int pIdx = endPIdx;
        boolean[] base = new boolean[3];

        while (outs < 3) {
            switch (playerEninig[eIdx][lineUp[pIdx]]) {
                case 0:
                    outs++;
                    break;

                case 1:
                    if (base[2])
                        result++;
                    for (int i = 2; i > 0; i--)
                        base[i] = base[i-1];
                    base[0] = true;
                    break;

                case 2:
                    for (int i = 1; i < 3; i++){
                        if (base[i])
                            result++;
                        base[i] = false;
                    }
                    if (base[0]){
                        base[2] = base[0];
                        base[0] = false;
                    }
                    base[1] = true;
                    break;

                case 3:
                    for (int i = 0; i < 3; i++){
                        if (base[i])
                            result++;
                        base[i] = false;
                    }
                    base[2] = true;
                    break;

                case 4:
                    for (int i = 0; i < 3; i++) {
                        if (base[i])
                            result++;
                        base[i] = false;
                    }
                    result++;
                    break;
            }
            pIdx = (pIdx + 1) % 9;
        }
        dfs(eIdx+1, result, pIdx);
    }

    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        playerEninig = new int[N][9];
        answer = 0;

        for (int eIdx = 0; eIdx < N; eIdx++){
            StringTokenizer st = new StringTokenizer(bf.readLine());
            for (int pIdx = 0; pIdx < 9; pIdx++) {
                playerEninig[eIdx][pIdx] = Integer.parseInt(st.nextToken());
            }
        }

        visit[0] = true;
        makeSeq(0);

        System.out.println(answer);
    }
}