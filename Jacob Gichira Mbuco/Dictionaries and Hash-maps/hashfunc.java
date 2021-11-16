/*
Implement a hash function hash(S) that takes in a string S and computes a hash value V based on every charater in the string S
*/
public class hashfunc {
    public static void main(String[] args) {
        String s = "hello";
        int hash = 0;
        for (int i = 0; i < s.length(); i++) {
            hash = hash + (int) s.charAt(i);
        }
        System.out.println(hash);
    }
    
}
