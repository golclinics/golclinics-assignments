

/**
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the 
input array in-place with O(1) extra memory.
*/

function removeElement(A,remove) {
    // while index i = 0 to last no-remove position
        // If index i has remove item
            // If if lastPos has remove item
                // decreament last position
                // continue to next while
            // swap value with the last non-remove position
            // increment index
            // decreament non-remove position
        //next while
    let index = 0;
    let lastPos = A.length -1;
    while (index < lastPos ) {
        if (A[index] == remove) {
            if (A[lastPos] == remove) {
                lastPos --;
                continue;
            }
            let temp = A[index];
            A[index] = A[lastPos];
            A[lastPos] = temp;
            index ++;
            lastPos --
        }
        index ++
    }
    console.log(A);
}

removeElement([3,1,3,4,3,6],3)