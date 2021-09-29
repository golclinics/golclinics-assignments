package com.arraysandstrings;



public class Main {






    public static void main(String[] args) {
	// write your code here
        int [] a = new int[]{1, 4, 5, 6};

        reverseArray(a);

    }


    /**
     *
     * @param a, integer array
     *   reverse the element of int array a
     */
    static void reverseArray( int []a){


        if(a.length==0) // check if the array is  empty
            return;

        for(int i=a.length-1; i>=0; i--) { // if not give print reversed

            if(i==a.length-1) {
                System.out.print("[ " + a[i]);
            }
            else {
                System.out.print("," + a[i]);
            }
        }
        System.out.print("]");

    }




}

