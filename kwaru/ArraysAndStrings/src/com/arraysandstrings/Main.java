package com.arraysandstrings;

public class Main {






    public static void main(String[] args) {

        int [] A = new int[]{10, 5, 6, 9};

       reverseArray(A);

    }


    /**
     *
     * @param a, integer array
     *   reverse the element of int array a
     */
    static void  reverseArray( int []a){
    int temp;
    int j=0;

        if(a.length==0) // check if the array is  empty
            return ;

          int  reverseTimes=a.length/2;
        for(int i=a.length-1; i>=0; i--) {

            temp= a[j];
            a[j]=a[i];
            a[i]=temp;
            j++;
            if(j==reverseTimes)
                break;


        }
        formatArray(a);// output array object
return ;





    }


    /**
     *
     * @param resultArray
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

