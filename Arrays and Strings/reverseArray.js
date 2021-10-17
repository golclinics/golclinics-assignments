function reverseArray(A){
    let leftIndex = 0;
    let rightIndex = A.length-1;
  
    while(leftIndex < rightIndex){
  
  //declares temp variable
      let temp = A[leftIndex];
      A[leftIndex] = A[rightIndex];
      A[rightIndex] = temp;
  
  //move indices to the middle
  leftIndex++;
  rightIndex--;
    }
  }
  let myArray = [1, 3, 2, 8, 23];
  let A = [10, 5, 6, 9];
  
  reverseArray(myArray);
  reverseArray(A);
  
  
  console.log(myArray);
  console.log(A);
  