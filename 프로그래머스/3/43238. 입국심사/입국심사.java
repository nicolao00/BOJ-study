//828
class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        long left = 1; long right = (long)times[times.length-1] * n;
            
        while (left <= right){
            long mid = (left + right)/2;
            long people = 0;
            for (int i=0; i < times.length; i++){
                people += (mid / times[i]);
            }
            
            if (people >= n) {
                right = mid - 1;
                answer = mid;
            }
            else {
                left = mid + 1;
            }
        }
            
        return answer;
    }
}

// 1 2 3 4 5 6 7 8 9 10 11
// 1           1 3
// 2                  2
    
// time[0](7) 7
// time[1](10) 0
// time[2]()
    
    
// time[-1](5) 5
// time[0](7) 7
// time[1](8) 8
// time[2](10) 10

// 28 
// 7 = 4
// 10 = 2       

// 20 -> 9
// 4 = 5
// 5 = 4

// 19 ->
// 4 = 4
// 5 = 3 
// // 18 ->
// 4 = 4
// 5 = 3
// 끝나는 시간을 기준으로 이분탐색하면 될거같은데