
const minimumSwaps = (arr) => {
    let n = arr.length;
    let i;
    let count = 0;
    for(i = 0; i < n; i++){
        const temp = arr[i + 1];
        const temp2 = arr[n-1]
        if(arr[i] > arr[i + 1]){
            arr[i + 1] = arr[i];
            arr[i] = temp;
            count++;
        }
       
    }

    for(i = 0; i < n; i++){
        for(let j = 0; j < n; j++){
            let temp = arr[j]
          if(arr[j] > arr[j + 1]){
              arr[j] = arr[j + 1]
              arr[j + 1] = temp
              count++
          }
        }
    }


    console.log(count);
    console.log(arr);

}

minimumSwaps([4,2,56,7,1,9])