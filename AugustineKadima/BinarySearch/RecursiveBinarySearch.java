public class RecursiveBinarySearch {
    public static void main(String[] args) {
        int[] numbers = {1, 3, 4, 5, 10, 11, 23, 50};

        boolean result = RecursiveBinarySearch.findElement(numbers, 1,5,0);
        System.out.println(result);
    }

    private static boolean findElement(int[] numbers, int val, int end, int start) {
        int n = numbers.length - 1;
        int midpoint = (int) n/2;
        start = 0;


        if(val < numbers[midpoint]){
            n = midpoint - 1;
            findElement(numbers, val, n, start);
        }else if(val > numbers[midpoint]){
            start = midpoint + 1;
            findElement(numbers, val, n, start);
        }

        return false;
    }
}
