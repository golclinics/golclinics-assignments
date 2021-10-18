var A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
reverseSentence(A)
// ['g','o','o','d',' ','i','s',' ','t','h','i','s']

function reverseSentence(arr){

    arr = arr.join('');
    arr = arr.split(' ');

    var start = 0;
    var stop = arr.length - 1;


    while (start < stop){
        var temp = arr[start];
        arr[start] = arr[stop];
        arr[stop] = temp;
        start++;
        stop--;
    }

    for(var i = 0; i < arr.length; i++){
        arr[i] = arr[i].split('');
    }

    arr = arr.join(', ,')

    console.log(arr)
}

