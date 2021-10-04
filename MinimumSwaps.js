var a = [7, 1, 3, 2, 4, 5, 6];
var b = [4, 3, 1, 2];
var c = [2, 3, 4, 1, 5];
var swaps = 0;

function minimumSwaps(arr){

    var isSwapped = false;

    for (var i = 0, len = arr.length; i < len; i ++){
        for (var j = 0; j < (len - i - 1); j ++){
            if (arr[j] > arr[j + 1]){
                swap(arr, j, j + 1);
                isSwapped = true;
                swaps++;
            }
        }

        if(!isSwapped){
            break;
        }
    }

    function swap (arr, position, next){
        [arr[position], arr[next]] = [arr[next], arr[position]];
    }

}

console.log(a);

minimumSwaps(a);

console.log(a);

console.log("no of swaps are: " + swaps);