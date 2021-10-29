`Write a function reverseSentence(A) that takes in an array of characters, A, 
and reverses the the "words" (not individual characters).`


   function reverseInPlace(arr) {
      for (var i = 0; i <= (arr.length / 2); i++) {
          let el = arr[i];
          arr[i] = arr[arr.length - 1 - i];
          arr[arr.length - 1 - i] = el;
      }
      return arr;
    }
  
  console.log(reverseInPlace(['t','h','i','s',' ','i','s',' ','g','o','o','d']))


