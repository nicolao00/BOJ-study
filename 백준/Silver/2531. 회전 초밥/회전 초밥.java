// 520
import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main{
    public static void main(String args[]) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        // 회전 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] belt = new int[N];
        for (int i=0; i<N;i++){
            belt[i] = Integer.parseInt(bf.readLine());
        }

        int start = 0;
        int end = k-1;
        int answer = 0;
        Map<Integer, Integer> dict = new HashMap<>();
        for (int i=0; i<k; i++){
            dict.put(belt[i], dict.getOrDefault(belt[i], 0) + 1);
        }
        while (start < N) {
            end++;
            if (end == N)
                end = 0;
            dict.put(belt[end], dict.getOrDefault(belt[end], 0) + 1);
            dict.put(belt[start], dict.get(belt[start])-1);
            if (dict.get(belt[start]) == 0){
                dict.remove(belt[start]);
            }
            start++;
            int result = dict.size();
            if (!dict.containsKey(c))
                result++;
            answer = Math.max(answer, result);
        }
        System.out.println(answer);
    }
}