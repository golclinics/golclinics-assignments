

const checkBalancedParantheses = (exp) => {
    const stack = []

    for (let i = 0; i < exp.length; i++) {
        const element = exp.charAt(i);
        const peek = stack[stack.length - 1];
        const length = stack.length
    
        if(element === ')' && peek === '('  && length !== 0){
            stack.pop();

        } else if(element === '}' && peek === '{'  && length !== 0){
            stack.pop();
            
        } else if(element === ']' && peek === '['  && length !== 0){
            stack.pop();
            
        } else {
            stack.push(element);
        }
   
    }

    console.log('Content of array are', stack);
    if (stack.length === 0)  return true; return false;
}

checkBalancedParantheses('{[]()}');
