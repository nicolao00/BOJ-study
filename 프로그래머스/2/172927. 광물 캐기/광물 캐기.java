import java.util.*;

class Solution {
    boolean[] visit;
    int[] pickArr;
    String[] minerals; 
    int answer = Integer.MAX_VALUE;

    int calcul(int groupIdx, int type) {
        int result = 0;
        for (int i = groupIdx * 5; i < Math.min(groupIdx * 5 + 5, minerals.length); i++) {
            switch (type) {
                case 0:
                    result += 1;
                    break;
                case 1:
                    if (minerals[i].equals("diamond"))
                        result += 5;
                    else
                        result += 1;
                    break;
                case 2:
                    if (minerals[i].equals("diamond"))
                        result += 25;
                    else if (minerals[i].equals("iron")) {
                        result += 5;
                    } else
                        result += 1;
                    break;
            }
        }
        return result;
    }

    // 목표 길이, 현재 인덱스, 길이, 값
    void makeComb(int goalLen, int len, int result) {
        if (result >= answer) {
            return;
        }
         if (len == goalLen) {
            answer = result;
            return;
        }

        for (int i = 0; i < goalLen; i++) {
            if (!visit[i]) {
                visit[i] = true;
                makeComb(goalLen,len + 1, result + calcul(len, pickArr[i]));
                visit[i] = false;
            }
        }
    }

    public int solution(int[] picks, String[] a) {
        minerals = a;

        int pickLen = Math.min((int) Math.ceil(minerals.length / 5.0), picks[0] + picks[1] + picks[2]);
        pickArr = new int[pickLen];

        int idx = 0;
        for (int type = 0; type < 3; type++) {
            for (int j = 0; j < picks[type] && idx < pickLen; j++) {
                pickArr[idx++] = type;
            }
            if (idx >= pickLen)
                break;
        }

        visit = new boolean[pickLen];
        makeComb(pickLen,0, 0);

        return answer;
    }

    
}
