

const reverseArray = (A) => {
    let n = A.length - 1;
    let i;
   
    for(i = 0; i < n; i++){
        let temp = A[n];
        if(i < n){
            A[n] = A[i];
            A[i] = temp;
            n--;
        }
    } 
    console.log(A);

}
reverseArray([9, 6, 5, 10, 7, 4, 3, 4, 5]);