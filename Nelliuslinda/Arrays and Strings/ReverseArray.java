package com.company;

public class Main {
    //Function to reverse Array
    static void reverseArray(int[] arr){
        int x = arr.length;
        for (int i=0; i< arr.length/2; i++){
            int temp = arr[i];
            arr[i]=arr[x-1-i];
            arr[x-1-i]=temp;
        }
        for (int j : arr) {
            System.out.println(j);
        }
       
    }

    //Driver function to reverse Array
    public static void main(String[] args) {
        int[] A = new int[]{10,5,6,9};
        System.out.println("The new reversed array is:");
        reverseArray(A);
    }
}
