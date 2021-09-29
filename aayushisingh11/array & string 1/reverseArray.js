var A = [10, 5, 6, 9]
function reverseArray(input){
    var reverse = new Array;
    for(var i = input.length-1; i>=0; i--){
        reverse.push(input[i]);
    }
    return reverse;
}
 var b = reverseArray(A);