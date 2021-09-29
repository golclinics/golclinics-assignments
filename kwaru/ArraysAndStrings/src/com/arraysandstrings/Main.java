package com.arraysandstrings;

public class Main {






    public static void main(String[] args) {

        int [] A = new int[]{10, 5, 6, 9};

       reverseArray(A);

    }


    /**
     *
     * @param A, integer array
     *   reverse the element of int array a
     *   Without using another array 
     */
    static void  reverseArray( int []A){
    int temp;
    int j=0;

        if(A.length==0) // check if the array is  empty
            return ;

          int  reverseTimes=A.length/2; // i need to perform reverse approximately length divide by times
                                         //to take of the last  sole element in case of odd number of elements


        for(int i=A.length-1; i>=0; i--) { // if not give print reversed

            temp= A[j];
            A[j]=A[i];
            A[i]=temp;
            j++;
            if(j==reverseTimes) // break when number reverses is reached
                break;


        }
        formatArray(A);// output array object
return ;





    }


    /**
     *
     * @param resultArray
     * print array nicely eg [,9,6,5,10]
     */
    static void formatArray(int []resultArray){
        int i=0;
        System.out.print("[");
        for(int k : resultArray){

            if(i==0)System.out.print(+k);// the first element should not have , before
            if(i>0)System.out.print(","+k);
            i++;
        }
        System.out.print("]");
    }

}

