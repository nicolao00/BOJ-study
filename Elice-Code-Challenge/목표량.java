//156
import java.util.*;
import java.io.*;

class Main {
    static int num;
    static int[] elements;
    static int answer;
    static boolean flag;
    static boolean[] visit;

    public static void dfs(int position, int value) {
        if (position == -1) {
            if (value > num){
                answer = value;
                flag = true;
            }
            return;
        }

        for (int i = 0; i < elements.length; i++) {
            if (flag)
                break;
            if (!visit[i]){
                // 백트래킹.
                int result = value + elements[i] * (int) Math.pow(10, position);
                if (num / Math.pow(10, position) > result)
                    continue;

                visit[i] = true;
                dfs(position-1, result);
                visit[i] = false;
            }
        }
    }


    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String str = bf.readLine();
        num = Integer.parseInt(str);
        elements = new int[str.length()];
        visit = new boolean[str.length()];
        answer = -1;

        for (int i = 0; i < str.length(); i++)
            elements[i] = str.charAt(i) - '0';

        Arrays.sort(elements);

        dfs(str.length()-1, 0);

        System.out.println(answer);
    }
}