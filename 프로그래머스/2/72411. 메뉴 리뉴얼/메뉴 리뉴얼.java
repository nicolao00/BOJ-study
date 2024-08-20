// 304
import java.util.*;

class Solution {

    static Map<String, Integer> combs = new HashMap<>();
    static char[] order;
    static boolean[] courseExist = new boolean[11];

    // 만들려는 길이, 현재 문자열, 현재까지 사용한 인덱스
    public void makeComb(StringBuilder tmp, int idx) {
        if (courseExist[tmp.length()]){
            String key = tmp.toString();
            combs.put(key, combs.getOrDefault(key, 0) + 1);
            if (tmp.length() >= order.length)
                return;
        }

        for (int i = idx; i < order.length; i++) {
            StringBuilder sb = new StringBuilder(tmp);
            makeComb(sb.append(order[i]), i+1);
        }
    }


    public String[] solution(String[] orders, int[] course) {
//        String[] answer1 = {};
        for (int a : course)
            courseExist[a] = true;

        for (String a : orders) {
            order = a.toCharArray();
            Arrays.sort(order);
            makeComb(new StringBuilder(), 0);
        }

        ArrayList<String>[] answers = new ArrayList[11];
        for (int i = 0; i < 11; i++)
            answers[i] = new ArrayList<>();
        int[] maxValues = new int[11];

        for (Map.Entry<String, Integer> set : combs.entrySet()){
            String key = set.getKey();
            int combCnt = set.getValue();

            if (combCnt >= 2){
                // 해당 course 값에서 새로운 가장 큰 값이 등장했을때
                if (maxValues[key.length()] < combCnt){
                    maxValues[key.length()] = combCnt;
                    answers[key.length()] = new ArrayList<>();
                    answers[key.length()].add(key);
                } else if (maxValues[key.length()] == combCnt) { // 해당 course값과 동일한 값이 등장했을 때
                    answers[key.length()].add(key);
                }
            }
        }

        int totalSize = 0;
        for (ArrayList<String> tmp : answers)
            totalSize += tmp.size();

        int sIdx = 0;
        String[] answer = new String[totalSize];
        for (int cIdx : course) {
            for (String str : answers[cIdx]) {
                answer[sIdx++] = str;
            }
        }

        Arrays.sort(answer);

        return answer;
    }
}