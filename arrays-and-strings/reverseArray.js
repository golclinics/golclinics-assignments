var A = [10, 5, 6, 9]
reverseArray(A)
// [9, 6, 5, 10]


function reverseArray(arr){
    var start = 0;
    var stop = arr.length - 1;
    var temp;

    while (start < stop){
        temp = arr[start];
        arr[start] = arr[stop];
        arr[stop] = temp;
        start++;
        stop--;
    }

    console.log(arr);
}

