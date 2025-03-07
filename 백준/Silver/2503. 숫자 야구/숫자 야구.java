import java.util.*;
import java.io.*;


// 441
class Main {
    static int N;
    static String[] numArr;
    static HashSet[] numSet;
    static boolean[] visit;
    static int[][] strikeBalls;
    static int answer;

    public static void dfs(StringBuilder nums) {
        if (nums.length() == 3){
            if (check(nums))
                answer += 1;
            return;
        }

        for (int i = 1; i <= 9; i++) {
            if (visit[i])
                continue;

            visit[i] = true;
            nums.append(i);
            dfs(nums);
            visit[i] = false;
            nums.deleteCharAt(nums.length()-1);
        }
    }

    public static boolean check(StringBuilder nums){
        int strike = 0;
        int ball = 0;

        for (int nIdx = 0; nIdx < N; nIdx++) {
            strike = 0;
            ball = 0;
            for (int i = 0; i < 3; i++) {
                if (nums.charAt(i) == numArr[nIdx].charAt(i)) {
                    strike++;
                } else if (numSet[nIdx].contains(nums.charAt(i))) {
                    ball++;
                }
            }
            if (strikeBalls[nIdx][0] != strike || strikeBalls[nIdx][1] != ball)
                return false;
        }
        return true;
    }

    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        numArr = new String[N];
        strikeBalls = new int[N][2];
        numSet = new HashSet[N];
        visit = new boolean[10];

        StringTokenizer st;
        for (int i = 0; i < N; i++){
            numSet[i] = new HashSet();
            st = new StringTokenizer(bf.readLine());
            numArr[i] = st.nextToken();
            for (int idx = 0; idx < 3; idx++) {
                numSet[i].add(numArr[i].charAt(idx));
            }
            strikeBalls[i][0] = Integer.parseInt(st.nextToken());
            strikeBalls[i][1] = Integer.parseInt(st.nextToken());
        }

        dfs(new StringBuilder());

        System.out.println(answer);
    }
}