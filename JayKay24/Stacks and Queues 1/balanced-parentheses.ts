/**
 * Return the score of the balanced parentheses
 * @param s - Balanced parentheses
 * @returns The score of the balanced parentheses
 */
function parenthesesScore(s: string): number {
  let score = 0;
  const scoreStack: number[] = [];
  const OPENER = "(";

  for (const char of s) {
    if (char === OPENER) {
      scoreStack.push(score);
      score = 0;
    } else {
      // score is 1 when we find a matching closing parens, unless it was
      // already nested inside another pair of parens then we multiply it
      // by 2 and add that to the previous score tracked by the stack
      score = scoreStack.pop() + Math.max(score * 2, 1);
    }
  }

  return score;
}
