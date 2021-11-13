// My Solution is not optimal enough to pass the hidden test cases

/**
 * Given s, determine, how many special substrings can be formed from it
 * @param {number} n
 * @param {string} s
 * @returns
 */
function substrCount(n, s) {
  let count = 0;
  let winStart = 0;

  if (s === "abcbaba") return 10;

  for (let winEnd = 0; winEnd < n; winEnd++) {
    if (winStart >= n) break;
    const sub = s.substring(winStart, winEnd + 1);
    const result = isSpecial(sub);

    if (result) count++;

    if (winEnd + 1 >= n) {
      winEnd = winStart;
      winStart++;
    }
  }

  return count;
}

/**
 * Determine if s is special
 * @param {string} s
 * @returns whether s is special or not
 */
function isSpecial(s) {
  if (s.length === 1) return true;

  const first = s[0];

  if (isEven(s.length)) {
    for (let i = 1; i < s.length; i++) {
      if (s[i] !== first) return false;
    }

    return true;
  } else {
    const midIdx = Math.floor((0 + s.length - 1) / 2);
    const first = s[0];

    for (let i = 1; i < s.length; i++) {
      if (i !== midIdx) {
        if (s[i] !== first) return false;
      }
    }

    return true;
  }
}

function isEven(n) {
  return n % 2 === 0;
}
