/*

Description:
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

DoubleChar("String") == "SSttrriinngg"

DoubleChar("Hello World") == "HHeelllloo  WWoorrlldd"

DoubleChar("1234!_ ") == "11223344!!__  "
Good Luck!
 */

using System.Text;

public class Kata
{
  public static string DoubleChar(string s)
  {
    StringBuilder sb = new StringBuilder();  
    for(int i = 0; i < s.Length; i++)
    {
      sb.Append(s[i]);
      sb.Append(s[i]);
    }
    return sb.ToString();
  }
}