// 618 - 29
// a b c d e f g h i j k l m n o p q r s t u v w x y z
class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        String abc = "abcdefghijklmnopqrstuvwxyz";
            
        for (int i = 0; i < skip.length(); i++){
            abc = abc.replace(String.valueOf(skip.charAt(i)), "");
        }
        
        
        for (int i = 0; i < s.length(); i++){
            int sIdx = abc.indexOf(s.charAt(i));
            answer += abc.charAt((sIdx + index)% abc.length());
        }
        
        
        return answer;
    }
}