﻿using System;
using Queues;

namespace Stacks
{
    class Program
    {
        static void Main(string[] args)
        {
          // var b0 = "()";
          // var b1 = "()[]{}";
          // var b2 = "(]";
          // var b3 = "([)]";
          // var b4 = "{[]}";
          // Console.WriteLine($"is {b0} valid? : {StackExercises.IsValid(b0)}");
          // Console.WriteLine($"is {b1} valid? : {StackExercises.IsValid(b1)}");
          // Console.WriteLine($"is {b2} valid? : {StackExercises.IsValid(b2)}");
          // Console.WriteLine($"is {b3} valid? : {StackExercises.IsValid(b3)}");
          // Console.WriteLine($"is {b4} valid? : {StackExercises.IsValid(b4)}");

          // //MinStack - Stacks & Queues Assignment 1
          // var minStack = new MinStack();
          // minStack.Push(-2);
          // minStack.Push(0);
          // minStack.Push(-3);
          // var min1 = minStack.GetMin();
          // minStack.Pop();
          // var top1 = minStack.Top();
          // var min2 = minStack.GetMin();

          // //MyStack - Stacks & Queues Assignment 2
          // var myStack = new MyStack();
          // myStack.Push(5);
          // myStack.Push(3);
          // myStack.Push(7);
          // myStack.Empty();
          // myStack.Top();
          // myStack.Empty();
          // myStack.Pop();
          // myStack.Top();
          // myStack.Pop();
          // myStack.Push(40);
          // myStack.Push(50);
          // myStack.Top();
          // myStack.Pop();
          // myStack.Empty();

          //MyQueue - Stacks & Queues Assignment 2
          var myQueue = new MyQueue();
          myQueue.Empty();
          myQueue.Push(5);
          myQueue.Push(12);
          myQueue.Push(20);
          myQueue.Peek();
          myQueue.Pop();
          myQueue.Pop();
          myQueue.Push(40);
        }


    }
}
