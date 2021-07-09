using System;

namespace Stacks_Class_Work_String
{
    class Program
    {
        static void Main(string[] args)
        {
            string naming = "Let Keep Growing to my Precise";

            char[] charNaming = naming.ToCharArray();

            Stack stack = new Stack(charNaming.Length);

            Stack newStack = new Stack(charNaming.Length);

            for (int t = 0; t < charNaming.Length; t++)
            {
                stack.push(charNaming[t]);
            }

            Console.Write($"The Word: ");

            stack.traverse();

            int i = charNaming.Length;

            while (i > 0)
            {
                char popped = stack.pop();

                newStack.push(popped);

                i--;
            }

            Console.Write($"\nThe Reverse Word: ");

            newStack.traverse();
        }
    }

    public class Stack
    {
        private char[] stack;

        private int top = -1;

        public Stack(int size)
        {
            stack = new char[size];
        }

        public void push(char val)
        {
            if (stackIsFull())
            {
                Console.WriteLine("Stack Overflow");
            }
            else
            {
                stack[++top] = val;
            }
        }

        private bool stackIsFull()
        {
            if (top == stack.Length)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        public char pop()
        {
            if (stackIsEmpty())
            {
                Console.WriteLine("Stack underflow");

                return 'f';
            }
            else
            {
                return stack[top--];
            }
        }

        private bool stackIsEmpty()
        {
            if (top == -1)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        public void peek()
        {
            if (stackIsEmpty())
            {
                Console.WriteLine("Stack Empty");
            }
            else
            {
                Console.Write(stack[top]);
            }
        }

        private void stackCapacity()
        {
            Console.WriteLine(top + 1);
        }

        public void traverse()
        {
            

            for (int i = 0; i <= top; i++)
            {
                Console.Write(stack[i] + " ");
            }
        }
    }
}