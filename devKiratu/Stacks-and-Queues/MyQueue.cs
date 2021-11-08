
using System.Collections.Generic;

namespace Queues
{
    public class MyQueue
    {
        // FIFO
      private Stack<int> mainStack = new Stack<int>();
      private Stack<int> helperStack = new Stack<int>();
      //Push -> pushes an element to the back of te queue
      public void Push(int val)
      {
         mainStack.Push(val);
      }
      //Peek -> returns the element at the front of the queue
      public int Peek()
      {
        var firstIn = int.MinValue;
        while(mainStack.Count > 0) 
        {
          firstIn = mainStack.Pop();
          helperStack.Push(firstIn);
        }
        while(helperStack.Count > 0)
        {
          var temp = helperStack.Pop();
          mainStack.Push(temp);
        }
        return firstIn;
      }
      //Pop -> removes element from the front of the queue and returns it
      public int Pop()
      {
        while(mainStack.Count > 1)
        {
          var temp = mainStack.Pop();
          helperStack.Push(temp);
        }
        var firstIn = mainStack.Pop();

        while(helperStack.Count > 0)
        {
          var temp = helperStack.Pop();
          mainStack.Push(temp);
        }

        return firstIn;
      }
      //Empty -> returns true if queue is empty else false
      public bool Empty()
      {
        return mainStack.Count == 0;
      }
    }
}
