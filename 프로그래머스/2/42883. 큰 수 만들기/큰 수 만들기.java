class Solution {
    public String solution(String number, int k) {
        int sIdx = 0;
        k = number.length() - k;
        StringBuilder sb = new StringBuilder();
        while (k > 0) {
            int maxV, maxI;
            maxV = -1; maxI = sIdx;
            for (int i = sIdx; i < number.length() - Math.max(k-1, 0); i++) {
                if (maxV < number.charAt(i)-'0'){
                    maxV = number.charAt(i)-'0';
                    maxI = i;
                    if (number.charAt(i)-'0' == 9)
                        break;
                }
            }
            k -= 1;
            if (sIdx >= number.length())
                break;
            
            sb.append(number.charAt(maxI)-'0');
            sIdx = maxI+1;
        }
        return sb.toString();
    }
}