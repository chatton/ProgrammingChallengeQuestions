/*

Description:
Your job is to create a calculator which evaluates expressions in Reverse Polish notation.

For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.

Note that for simplicity you may assume that there are always spaces between numbers and operations, e.g. 1 3 + expression is valid, but 1 3+ isn't.

Empty expression should evaluate to 0.

Valid operations are +, -, *, /.

You may assume that there won't be exceptional situations (like stack underflow or division by zero).

*/

import java.util.*;
public class Calc {

  public double evaluate(String expr) {
     if(expr.equals("")){
       return 0;
     }
     
    Stack<String> stack = new Stack();
    String[] tokens = expr.split(" ");
    for(String token : tokens){
      switch(token){
        case "+":{
          
          float token1 = Float.parseFloat(stack.pop());
          float token2 = Float.parseFloat(stack.pop());
          stack.push("" + (token1 + token2));
          break;
          }
        case "-": {
          float token1 = Float.parseFloat(stack.pop());
          float token2 = Float.parseFloat(stack.pop());
          stack.push("" + (token2 - token1));
          break;
          }
        case "*": {
          float token1 = Float.parseFloat(stack.pop());
          float token2 = Float.parseFloat(stack.pop());
          stack.push("" + (token1 * token2));
          break;
          }
        case "/":{
          float token1 = Float.parseFloat(stack.pop());
          float token2 = Float.parseFloat(stack.pop());
          stack.push("" + (token2 / token1));
          break;
          }
        default:
          stack.push(token);
      }
    }
    return Float.parseFloat(stack.pop());
  }
}