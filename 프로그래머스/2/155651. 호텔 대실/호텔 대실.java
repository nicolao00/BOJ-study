import java.util.*;

class Solution { 
    public class TimeInfo {
        int[] h;
        int[] m;

        public TimeInfo(String[] str) {
            h = new int[2];
            m = new int[2];
            for (int i = 0; i < 2; i++){
                h[i] = Integer.parseInt(str[i].substring(0, 2));
                m[i] = Integer.parseInt(str[i].substring(3, 5));
            }
        }
    }

    public void cleanup(TimeInfo tI) {
        tI.m[1] += 10;
        if (tI.m[1] >= 60){
            tI.h[1]++;
            tI.m[1] %= 60;
        }
    }
    public boolean compare(TimeInfo t1, TimeInfo t2){
        // 청소 끝시간보다 입실이 늦을때
        if (t1.h[1] < t2.h[0] || (t1.h[1] == t2.h[0] && t1.m[1] <= t2.m[0]))
            return true;
        else
            return false;
    }

    public int solution(String[][] book_time) {
        int answer = 0;
        Arrays.sort(book_time, (o1, o2) -> (o1[0].compareTo(o2[0]) == 0) ? (o1[1].compareTo(o2[1])) : (o1[0].compareTo(o2[0])));


        PriorityQueue<TimeInfo> q = new PriorityQueue<>((t1, t2) -> {
            if (t1.h[1] != t2.h[1]) return t1.h[1] - t2.h[1];
            return t1.m[1] - t2.m[1];
        });
        TimeInfo ti = new TimeInfo(book_time[0]);
        cleanup(ti);
        q.offer(ti);
        answer++;

        for (int i = 1; i < book_time.length; i++) {
            TimeInfo tmp = q.peek();
            TimeInfo nti = new TimeInfo(book_time[i]);
            // 청소 끝시간보다 입실이 늦을때
            if (compare(tmp, nti))
                q.poll();
            else
                answer++;
            cleanup(nti);
            q.offer(nti);
        }
        return answer;
    }
}