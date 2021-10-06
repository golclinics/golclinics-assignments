using System;

namespace Stacks_Class_Work
{
    class Program
    {
        static void Main(string[] args)
        {
            Stack stack = new Stack(6);

            stack.push(4);
            stack.push(3);
            stack.push(9);
            stack.push(3);
            stack.push(3);
            stack.pop();
            stack.pop();
            stack.pop();
            stack.pop();
            stack.push(1);

            Console.WriteLine($"Mininum value is { stack.getMinValue }");
        }
    }

    public class Stack
    {
        private int _capacity = 0;

        private int[] _newStack;

        private int count = 0;

        private int _getMin = 0;

        private int _temp;

        public Stack(int size)
        {
            this._newStack = new int[size];
        }

        public void push(int value)
        {
            if(_capacity == _newStack.Length)
            {
                Console.WriteLine("Stack Full");
                return;
            }

            _newStack[_capacity] = value;
            _capacity++;

            if(_getMin == 0)
            {
                _getMin = value;

                return;
            }

            if(_getMin == value)
            {
                count++;

                return;
            }

            if (_getMin > value)
            {
                _temp = _getMin;

                _getMin = value;

                return;
            }
        }

        public void pop()
        {
            if(_capacity == 0)
            {
                Console.WriteLine("Stack underflow");

                return;
            }

            _capacity--;

            if (_getMin == _newStack[_capacity])
            {
                if(count > 0)
                {
                    return;
                }

                _getMin = _temp;

                return;
            }
          
            return;
        }

        public int getMinValue
        {
            get
            {
                return _getMin;
            }
        }
    }
}