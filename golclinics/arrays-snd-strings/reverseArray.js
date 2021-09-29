const ReverseArray = (a) => {
  let left = 0;
  let right = a.length - 1;
  while (left < right) {
    swap(a, left, right);
    left++;
    right--;
  }
  return a;
};

function swap(arr, left, right) {
  let temp = arr[left];
  arr[left] = arr[right];
  arr[right] = temp;
}

console.log(ReverseArray([1, 4, 5, 6]));
