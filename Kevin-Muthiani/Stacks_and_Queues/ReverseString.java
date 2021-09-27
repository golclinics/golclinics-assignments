import stacks.CharStack;


public class ReverseString{

	private static String inputString;

	public static void readString() {
		System.out.print("Enter string: ");
		inputString = System.console().readLine();
	}

	public static void reverseString() {
		// push string into stack
		for (var i=0; i<inputString.length(); i++) {
			CharStack.push(inputString.charAt(i));
		}

		// pop string from stack
		System.out.print("Reversed string: ");
		for (var i=0; i<inputString.length(); i++) {
			var charValue = CharStack.peek();
			System.out.print(charValue);
			CharStack.pop();
		}
		System.out.println("");
	}

	public static void main(String[] args){
		readString();
		reverseString();
	}
}
