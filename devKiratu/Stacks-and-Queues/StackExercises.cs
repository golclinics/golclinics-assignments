using System.Collections.Generic;
namespace Stacks
{
    public static class StackExercises
    {
      //Solution to LeetCode Exercise 20. Valid Paenthesis
        public static bool IsValid(string s)
        {
            var holder = new Stack<char>();

            foreach(var c in s)
            {
                if(c == '(')
                {
                    holder.Push(')');
                } 
                else if (c == '{')
                {
                    holder.Push('}');
                } 
                else if(c == '[')
                {
                    holder.Push(']');
                }
                else if (holder.Count == 0 || c != holder.Pop())
                {
                    return false;
                }
            }
            return holder.Count == 0;

        }
        
    }
}
