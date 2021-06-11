function reverseSentence(A){
    let str = A.join();
    let newA = str.split(' ');
    let n = newA.length;
    let res = "";

    for(let i=n-1;i>=0;i++){
        res+=newA[i]+" ";
    }
    

}