using System;
namespace Stacks
{
    public class MinStack
    {
    private int[] holder;
    private int[] minValHolder;
    private int index;
    private int minIndex;
    public MinStack()
    {
      holder = new int[5];
      minValHolder = new int[5];
      Array.Fill(holder, int.MinValue);
      Array.Fill(minValHolder, int.MinValue);
      index = holder.Length - 1;
      minIndex = minValHolder.Length - 1;
    }
    public void Push(int val)
    {
      if (index >= 0) 
      {
        holder[index] = val;
        index--;
        if (minIndex == minValHolder.Length-1 && minValHolder[minIndex] == int.MinValue)
        {
          minValHolder[minIndex] = val;
        } 
        else if (minIndex >= 0 && minValHolder[minIndex] >= val)
        {
          minIndex--;
          minValHolder[minIndex] = val;
        }
      }
      else 
      {
        throw new InvalidOperationException("The Stack is full");
      }
    }

    public void Pop()
    {
      if(GetMin() == Top()) 
      {
        minValHolder[minIndex] = int.MinValue;
        minIndex++;
      }
      holder[++index] = int.MinValue;
    }

    public int Top() 
    {
       return holder[index+1]; 
    }

    public int GetMin() 
    {
       return minValHolder[minIndex]; 
    }

  }
}
