/*

Bonus:
 Implement a function histogram(S) that takes in a string S and plots a histogram of words in the sentence:
# e.g Given a sentence S:   "Life is so so good", plot

Life: *
is:   *
so:   **
good: *
*/
public class histo {
    public static void main(String[] args) {
        String s = "Life is so so good";
        histogram(s);
    }

    public static void histogram(String s) {
        String[] words = s.split(" ");
        for (String word : words) {
            System.out.print(word + ": ");
            for (int i = 0; i < word.length(); i++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
    
}
