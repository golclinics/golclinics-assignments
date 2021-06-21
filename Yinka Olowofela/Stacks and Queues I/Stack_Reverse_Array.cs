using System;

namespace Stacks_Class_Work_Two
{
    class Program
    {
        static void Main(string[] args)
        {
            Stack stack = new Stack(7);

            Stack newStack = new Stack(7);

            stack.push(2);
            stack.push(4);
            stack.push(11);
            stack.push(25);
            stack.push(17);
            stack.push(14);
            stack.push(7);

            stack.traverse();

            int i = 7;

            while (i > 0)
            {
                int popped = stack.pop();

                newStack.push(popped);

                i--;
            }

            newStack.traverse();
        }       
    }

    public class Stack
    {
        private int[] stack;

        private int top = -1;

        public Stack(int size)
        {
            stack = new int[size];
        }

        public void push(int val)
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

        public int pop()
        {
            if (stackIsEmpty())
            {
                Console.WriteLine("Stack underflow");

                return -1;
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