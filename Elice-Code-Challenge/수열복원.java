// 611
import java.util.*;
import java.io.*;

class Main {
    static int N;
    static long[] arr;
    static long[] answer;
    static int aIdx;
    // 만들 수 있는 값과 횟수
    static Map<Long, Integer> sumMap;
    // 주어진 수열의 각 값들의 개수
    static Map<Long, Integer> ansMap;

    public static void check(long value) {
//        원소 등록 기준
//        : 등록된 조합에 존재하는지
//                - 존재한다면 횟수가 동일한지
//        등록되지 않았다면
//        원소 등록
//        - 기존에 있는 원소들에 새로운 원소들 더해서 모든 조합을 키에 저장 및 횟수 ++

        // 원소 등록 필요한 경우
        if (!sumMap.containsKey(value) || sumMap.get(value) < ansMap.get(value)){
            Map<Long, Integer> tmp = new HashMap<>();
            answer[aIdx++] = value;
            // 기존 값들에 새로운 값을 추가하는 과정
            for (Map.Entry<Long, Integer> object : sumMap.entrySet()) {
                for (int i = 0; i < object.getValue(); i++) {
                    long sum = object.getKey() + value;
                    tmp.put(sum, tmp.getOrDefault(sum, 0) + 1);
                }
            }
            for (Map.Entry<Long, Integer> object : tmp.entrySet())
                sumMap.put(object.getKey(), sumMap.getOrDefault(object.getKey(), 0) + object.getValue());
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        arr = new long[(int)Math.pow(2, N)];
        answer = new long[N];
        sumMap = new HashMap<>();
        ansMap = new HashMap<>();
        aIdx = 0;

        StringTokenizer st = new StringTokenizer(bf.readLine());
        for(int i = 0; i < (int)Math.pow(2, N); i++)
            arr[i] = Long.parseLong(st.nextToken());

        Arrays.sort(arr);

        sumMap.put((long)0, 1);
        for (int i = 1; i < arr.length; i++) {
            ansMap.put(arr[i], ansMap.getOrDefault(arr[i], 0) + 1);
            check(arr[i]);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(answer[i]);
            if (i != N-1)
                sb.append(' ');
        }
        System.out.println(sb.toString());
    }
}