

const reverseSentence = (A) => {
    let n = A.length -1;
    let i;
    
    for(i =0; i < n; i++){
        let temp = A[n];
        if(i < n){
            A[n] = A[i];
            A[i] = temp;
            n--;
        }
    }

    let positionOfSpace = A.indexOf(" ");
    let j = 0;
    for(j; j < positionOfSpace; j++){
        let temp = A[positionOfSpace - 1];
        A[positionOfSpace - 1] = A[j];
        A[j] =temp;
        positionOfSpace--  
        
    }
}

reverseSentence(['t','h','i','s',' ','i','s',' ','g','o','o','d']);