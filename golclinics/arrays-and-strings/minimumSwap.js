function minSwaps(arr){
   let ans = 0;

  let n = arr.length;

//returns element and position of the element
  let arrPosition = [];
  for(let i = 0; i<n; i++){
    arrPosition.push([arr[i], i]);
  }
   arrPosition.sort(function(a,b){
    return a[0]-b[0];
   });

   let vis = new Array(n);
   for(let i =0; i<n; i++){
     vis[i]= false;
   }

  

   for(let i = 0; i<n; i++){

     if(vis[i] || arrPosition[i][1] == i)
     continue;
   

//find out the number of  node in this cycle
   let cycle_size = 0;
  let j = i;
   while(!vis[j]){

     vis[j] = true;

     //move to next node

     j = arrPosition[i][1];

     cycle_size++;
   }
  
   if(cycle_size > 0){
     ans+=(cycle_size-1);
   }
   }
   return ans;

 

}

console.log(minSwaps([7,4,5,2,1,3,6]));

//GeekforGeek