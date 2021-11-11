function reverse(str) {
    let stack = [];
    for (let i = 0; i < str.length; i++) {
        stack.push(str[i]);
    }
    let reverseStr = '';
    while (stack.length > 0) {
        reverseStr += stack.pop();
    }
    return reverseStr;
}
console.log(reverse('GOL CLINICS')); 