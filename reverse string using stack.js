



const reverseString = (string) => {
    let stack = [];
    for (let i = 0; i < string.length; i++) {
        stack.push(string.charAt(i))
        
    }
    
    let reversedString = '';
    
    for (let i = stack.length - 1 ; i >= 0; i--) {
        reversedString += stack[i];
        
    }
    
    return reversedString;
}
console.log(reverseString('felix'));
