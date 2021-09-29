function reverseSentence(A){

let NewStringArray = [];

for(let i = A.length-1; i>=0; i--){
  NewStringArray.push(A[i]);
}
return NewStringArray.join('');
}
 console.log(reverseSentence('string'));