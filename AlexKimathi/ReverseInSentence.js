
    function reverse(str,start,end)
    {
    
        let temp;
         
         
        while (start <= end)
        {
            // Swap first and last//
            temp = str[start];
            str[start]=str[end];
            str[end]=temp;
            start++;
            end--;
        }
    }
   
    function reverseWords(s)
    {
    
        s=s.split("");
        let start = 0;
        for (let end = 0; end < s.length; end++)
        {
          
            if (s[end] == ' ')
            {
                reverse(s, start, end);
                start = end + 1;
            }
        }
        // Reverse the last word//
        reverse(s, start, s.length - 1);
         
        // Reverse the entire String//
        reverse(s, 0, s.length - 1);
        return s.join("");
    }
  
    var s = " 't','h','i','s',' ','i','s',' ','g','o','o','d' ";
     
    console.log(reverseWords(s));
     
