using System;

namespace Stack_Ass_1
{
    class Program
    {
        static int stackSize = 4;

        static int newStackSize = 10;

        static int[] stack = new int[stackSize];

        static int[] newStack = new int[newStackSize];

        static int top = -1;

        static void Main(string[] args)
        {
            push(5);
            push(7);
            push(4);
            push(9);

            Console.Write("Stack: ");

            traverse();
            Console.WriteLine("");

            push(12);

            Console.Write("New Stack: ");
            traverseAdd();

            Console.WriteLine("");

            newPush(6);
            traverseAdd();

            Console.WriteLine("");

            Console.Write("Peek: ");
            peek();

            Console.WriteLine("");

            Console.Write("Capacity: ");
            stackCapacity();

            //pop();
            //traverse();

            //Console.WriteLine("");

            //stackCapacity();

            //traverseAdd();
        }

        static void push(int val)
        {
            if (stackIsFull())
            {
                Console.WriteLine("Stack Overflow");

                stack.CopyTo(newStack, 0);

                newPush(val);
            }
            else
            {
                stack[++top] = val;
            }
        }

        static bool stackIsFull()
        {
            if (top == stackSize - 1)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        static void newPush(int val)
        {
            if (newStackIsFull())
            {
                Console.WriteLine("Stack Overflow");
            }
            else
            {
                newStack[++top] = val;
            }
        }

        static bool newStackIsFull()
        {
            if (top == newStackSize - 1)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        static void pop()
        {
            if (stackIsEmpty())
            {
                Console.WriteLine("Stack underflow");
            }
            else
            {
                top--;
            }
        }

        static bool stackIsEmpty()
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

        static void peek()
        {
            if (stackIsEmpty())
            {
                Console.WriteLine("Stack Empty");
            }
            else
            {
                Console.Write(newStack[top]);
            }
        }

        static void stackCapacity()
        {
            Console.WriteLine(top + 1);
        }

        static void traverse()
        {
            for (int i = top; i >= 0; i--)
            {
                Console.Write(stack[i] + " ");
            }
        }

        static void traverseAdd()
        {
            for (int i = top; i >= 0; i--)
            {
                Console.Write(newStack[i] + " ");
            }
        }
    }
}