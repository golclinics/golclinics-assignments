// Time complexity
// The time complexity is Linear since we have a while loop that loops over
// n times. The number of operation increses proportionaly with the increase in the value of the 
// input value n

//For a worst case scenario. 
  // The trend would be increase linearly.

// Examples
countDown(5) // number of operation equal to 5 times
countDown(6) // number of operation equal to 6 times
countDown(1000) // number of operation equal to 1000 times.

function countDown(n){
   while(n > 0){
      console.log(n)
     n-=1;
   }
   console.log("Blast off")
}
