var A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
function reverseString(input){
    var reverse = new Array;
    for(var i = input.length-1; i>=0; i--){
        reverse.push(input[i]);
    }
    return reverse;
}
 var b = reverseString(A);