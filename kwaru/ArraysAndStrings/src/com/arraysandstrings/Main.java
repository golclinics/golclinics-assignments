package com.arraysandstrings;

public class Main {






    public static void main(String[] args) {

        int [] A = new int[]{4 ,3 ,1 ,2};

       reverseArray(A);

        char []charArray = new char[]{'t','h','i','s',' ','i','s',' ','g','o','o','d'};

        rotateStringArray(charArray);

        
        formatArrayStr(charArray);

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






    public  static void rotateChar(int startIndex, int endIndex,char[]array){
        char temp=' ';
        for(int y =startIndex; y<endIndex;y ++){
            temp= array[y];
            array[y]=array[endIndex];
            array[endIndex]=temp;
            endIndex--;

        }

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

   static void formatArrayStr(char []resultArray){
        int i=0;
        System.out.print("[");
        for(char k : resultArray){

            if(i==0)System.out.print(k);// the first element should not have , before
            if(i>0)System.out.print(","+k);
            i++;
        }
        System.out.print("]");
    }





    /**
     *
     * A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
     * reverseSentence(A)
     * A // ['g','o','o','d',' ','i','s',' ','t','h','i','s']
     *
     * @param array
     */
    public static char [] rotateStringArray(char [] array){
        char temp=' ';
        int i =0;
        int j= array.length-1;
        for( i =0;i< array.length; i++){

            if(array[i]==' ')
                break;
            temp=array[i];
            array[i]=array[j];
            array[j]=temp;

            j--;

        }
        rotateChar(0,i-1,array);
        rotateChar(j+1,array.length-1,array);

        return array;
    }




    /**
     *
     * @param array
     * @param i
     * @param j
     * @return
     */

    public int swapElements(int array[],int i , int j){
        if(i==j)
            return 0;


        int temp = array[i];
        array[i]= array[j];
        array[j]=temp;

        return 1; }



    /**
     *
     * @param a
     * @return mini number of swap operations
     */

    public  int minimumSwaps(int[] a) {
        int swap=0;
        for(int i=0;i<a.length;i++){
            if(i+1!=a[i]){
                int t=i;
                while(a[t]!=i+1){
                    t++;
                }
                int temp=a[t];
                a[t]=a[i];
                a[i]=temp;
                swap++;
            }
        }
        return swap;

    }

}

