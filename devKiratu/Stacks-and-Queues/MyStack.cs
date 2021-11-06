using System.Collections.Generic;
namespace Stacks
{
    public class MyStack
    {
      //LIFO
      private Queue<int> mainQueue = new Queue<int>();
      private Queue<int> helperQueue = new Queue<int>();

      //Push -> pushes element to top of Stack
      public void Push(int val)
      {
        mainQueue.Enqueue(val);
      }

      //Pop -> removes element from top of stack and returns it
      public int Pop()
      {
        while(mainQueue.Count > 1)
        {
          var temp = mainQueue.Dequeue();
          helperQueue.Enqueue(temp);
        }

      var lastIn = mainQueue.Dequeue();
      
      while(helperQueue.Count > 0)
      {
        var temp = helperQueue.Dequeue();
        mainQueue.Enqueue(temp);
      }
      return lastIn;
    }
      //Top -> returns the element on top of the stack
      public int Top()
      {
        int top = int.MinValue;
        while(mainQueue.Count > 0)
        {
          top = mainQueue.Dequeue();
          helperQueue.Enqueue(top);
        }
        while(helperQueue.Count > 0)
        {
          var temp = helperQueue.Dequeue();
          mainQueue.Enqueue(temp);
        }
      return top;
    }
      //Empty -> returns true if stack is empty, else false
      public bool Empty()
      {
        return mainQueue.Count == 0;
      }
  }
}
