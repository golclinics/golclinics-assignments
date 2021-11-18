//Insertion sort (research, reading, implementation)
//implementation of insertion sort

public class insertion {
    public static void main(String[] args) {
        int[] array = {1, 4, 3, 2, 5, 6, 7, 8, 9, 10};
        int[] sorted = insertionSort(array);
        for (int i = 0; i < sorted.length; i++) {
            System.out.println(sorted[i]);
        }
    }
    
    public static int[] insertionSort(int[] array) {
        for (int i = 1; i < array.length; i++) {
            int j = i;
            while (j > 0 && array[j] < array[j - 1]) {
                int temp = array[j];
                array[j] = array[j - 1];
                array[j - 1] = temp;
                j--;
            }
        }
        return array;
    }

    
}

