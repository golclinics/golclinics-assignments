// Bracket characters: (, ), {, }, [, or ]

import stacks.CharStack;


public class CheckBracketBalance{

	private static String bracketSequence;
	private static char[] openingBrackets = { '(', '{', '[' };
	// private static char[] openingBrackets = { '(', '{', '[' };

	public static void setSequence(String bracketString) {
		bracketSequence = bracketString;
	}

	public static boolean isBalanced() {
		for (var i=0; i<bracketSequence.length(); i++) {
			var bracket = bracketSequence.charAt(i);

			// Check if bracket is an opening one.
			if (new String(openingBrackets).indexOf(bracket) >= 0) {
				// Push bracket into stack
				CharStack.push(bracket);
			} else {
				// Check if bracket closes the last opening bracket pushed into stack
				var openingBracket = CharStack.peek();
				boolean isRoundBrackets = ((openingBracket == '(') && (bracket == ')'));
				boolean isCurlyBrackets = ((openingBracket == '{') && (bracket == '}'));
				boolean isSquareBrackets = ((openingBracket == '[') && (bracket == ']'));

				if (isRoundBrackets || isCurlyBrackets || isSquareBrackets) {
					CharStack.pop();
				} else {
					return false;
				}
			}
			// CharStack.traverse();
		}

		// return true if all opening brackets have been closed
		return (CharStack.capacity() == 0);
	}

	public static void main(String[] args){
		setSequence("{[()]}");
		System.out.println(isBalanced());

		setSequence("{[()]");
		System.out.println(isBalanced());

		setSequence("{[(])}");
		System.out.println(isBalanced());
	}
}
