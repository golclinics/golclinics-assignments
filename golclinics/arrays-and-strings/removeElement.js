function removeElement(arr, n){

  let i = 0;
    for (let j = 0; j < arr.length; j++) {
        // Swap numbers if current number is not equal to n
        if (arr[j] !== n) {
            arr[i] = arr[j];
            // Index where numbers that are equal to n begin in the array
            i++;
        }
    }
    return i;
};

console.log(removeElement([3,2,2,3],3));