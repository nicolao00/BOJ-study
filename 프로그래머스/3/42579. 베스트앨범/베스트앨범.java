// 148
import java.util.*;

class Solution {
    static Map<String, Integer> genreCnt = new HashMap<>(); // class: 6000번
    static Map<String, ArrayList<int[]>> genreSong = new HashMap<>(); // classic: {500번, 고유 2번}, {700번, 고유 3번}
    static ArrayList<Integer> answer = new ArrayList<>();


    public static void selectTwo(String genre) {
        if (genreSong.get(genre).size() == 1) {
            answer.add(genreSong.get(genre).get(0)[1]);
            return;
        }

        int exIdx = -1;
        for (int t = 0; t < 2; t++) {
            int maxV = -1;
            int maxI = -1;
            for (int[] cntIdx : genreSong.get(genre)){
                if (exIdx != cntIdx[1])
                    if (cntIdx[0] > maxV || (cntIdx[0] == maxV && cntIdx[1] < maxI)){
                        maxV = cntIdx[0];
                        maxI = cntIdx[1];
                    }
            }
            answer.add(maxI);
            exIdx = maxI;
        }

    }

    public int[] solution(String[] genres, int[] plays) {

        for (int i = 0; i < genres.length; i++) {
            genreCnt.put(genres[i], genreCnt.getOrDefault(genres[i], 0) + plays[i]);

            if (!genreSong.containsKey(genres[i]))
                genreSong.put(genres[i], new ArrayList<>());
            genreSong.get(genres[i]).add(new int[]{ plays[i], i });
        }


        // 재생횟수: 장르
        Map<Integer, String> cntGenre = new HashMap<>();
        Integer[] cntArr = new Integer[genreCnt.size()];
        int idx = 0;
        for (Map.Entry<String, Integer> es : genreCnt.entrySet()) {
            cntGenre.put(es.getValue(), es.getKey());
            cntArr[idx++] = es.getValue();
        }
        Arrays.sort(cntArr, Collections.reverseOrder());

        for (int i = 0; i < genreCnt.size(); i++) {
            String genre = cntGenre.get(cntArr[i]);
            selectTwo(genre);
        }
        
        int[] result = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++)
            result[i] = answer.get(i);
        return result;
    }
}