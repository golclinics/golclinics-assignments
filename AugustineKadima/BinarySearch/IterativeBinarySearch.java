public class IterativeBinarySearch {

    public static void main(String[] args) {
        int[] numbers = {1, 3, 4, 5, 10, 11, 23, 50};

        boolean result = IterativeBinarySearch.findElement(numbers, 1);
        System.out.println(result);
    }

    private static boolean findElement(int[] numbers, int val) {
        int n = numbers.length -1;
        int start = 0;

        if(n + 1 == 0){
            return false;
        }
        while( start <= n){
            int midpoint = n/2;
            if(val == numbers[midpoint] || val == numbers[start] || val == numbers[n]){
                return true;
            }
            if(numbers[midpoint] < val){
                start = midpoint + 1;
            }else if(numbers[midpoint] > val){
                n = midpoint - 1;
            }
        }
        return false;
    }
}
