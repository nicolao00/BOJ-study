// 835
import java.io.*;
import java.util.*;

class Main {
    static int N;
    static Set<Character> goalWords;
    static int[] goalWordCnt;
    // 각 책의 알파벳별 개수
    static int[][] bookWordCnt;
    static boolean[] visit;
    static int[] prices;
    static int minCost = 1600001;

    public static void dfs(int depth, int goalDepth, int bookIdx, int[] visitWordCnt, int cost) {
        // 이미 최소가격 넘었을때
        if (cost >= minCost)
            return;
        // 선택해야할 책 개수 됐을 때
        if (depth == goalDepth) {
            boolean flag = true;
            for (char word : goalWords){
                if (goalWordCnt[word-'A'] > visitWordCnt[word - 'A']){
                    flag = false;
                    break;
                }
            }
            if (flag)
                minCost = Math.min(cost, minCost);
            return;
        }

        for (int bIdx = bookIdx; bIdx < N; bIdx++) {
//            if (visit[bIdx])
//                continue;
//            visit[bIdx] = true;
            for (char word : goalWords)
                visitWordCnt[word - 'A'] += bookWordCnt[bIdx][word - 'A'];
            dfs(depth+1, goalDepth, bIdx + 1, visitWordCnt, cost + prices[bIdx]);
//            visit[bIdx] = false;
            for (char word : goalWords)
                visitWordCnt[word - 'A'] -= bookWordCnt[bIdx][word - 'A'];
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String answer = bf.readLine();

        goalWords = new HashSet<>();
        goalWordCnt = new int[26];

        for(int i = 0; i < answer.length(); i++){
            char word = answer.charAt(i);
            goalWords.add(word);
            goalWordCnt[word - 'A']++;
        }

        N = Integer.parseInt(bf.readLine());
        bookWordCnt = new int[N][26];
        prices = new int[N];

        for (int bookIdx = 0; bookIdx < N; bookIdx++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            prices[bookIdx] = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            for (int j = 0; j < name.length(); j++) {
                char word = name.charAt(j);
                bookWordCnt[bookIdx][word - 'A']++;
            }
        }

        for (int len = 1; len <= N; len++) {
//            visit = new boolean[N];
            dfs(0, len, 0, new int[26], 0);
        }
        if (minCost != 1600001)
            System.out.println(minCost);
        else
            System.out.println(-1);
    }
}


//a b c d e / f g h i j / k l m n o / p q r s t / u v W X Y / Z




