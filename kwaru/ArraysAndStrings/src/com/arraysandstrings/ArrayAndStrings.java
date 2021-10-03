package com.arraysandstrings;

/**
 * @author momondi  on 10/1/2021
 **/
public class ArrayAndStrings {
    public  ArrayAndStrings(){

    }
//['t','h','i','s',' ','i','s',' ','g','o','o','d']

    public static void reverseArrayofStrings(String [] A){
        int j=A.length;
        char temp =' ';
        for(int i =0;i<A.length;i++){
            if(A[i-1].equals(' ')&&A[j+1].equals(' '));
        }

    }

    public  int Sorting(int anyarray[]){
        int swapCounter=0;

        for(int lastUnsorted = anyarray.length-1; lastUnsorted>0; lastUnsorted--){

            for(int i =0; i<lastUnsorted;i++){
                if(anyarray[i]>anyarray[i+1])//{
                {
                        System.out.println("Swap is done and value of swapcounter is ->"+ swapCounter);
                        if(swapElements(anyarray,i,i+1)==1)
                        swapCounter++;
                }

            }


        }
        return swapCounter;
    }

    public  int insertionSort(int []array) {
        // improved Buble sort
        // 4
        //4 3 1 2
        // 0,2 => 1,3,4,2
        //1,3=>1,2,4,3
        //2,3=>
        //
        int swaps=0;
        int newElement = 0;
        for (int firstUnsortedElement = 0; firstUnsortedElement < array.length; firstUnsortedElement++) {

            newElement = array[firstUnsortedElement];
            int i = 0;
            for (i = firstUnsortedElement; i <array.length; i++) {
                array[i] = array[i - 1];

            }
            array[i] = newElement;
        }
return swaps;
    }




    public int swapElements(int array[],int i , int j){
        if(i==j)
            return 0;


        int temp = array[i];
        array[i]= array[j];
        array[j]=temp;

   return 1; }
}
