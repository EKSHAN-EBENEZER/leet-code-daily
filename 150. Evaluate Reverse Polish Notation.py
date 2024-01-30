'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Stack for storing numbers
        number_stack = []
      
        # Loop over each token in the input list
        for token in tokens:
            # If the token represents a number (accounting for negative numbers)
            if len(token) > 1 or token.isdigit():
                # Convert the token to an integer and push it onto the stack
                number_stack.append(int(token))
            else:
                # Perform the operation based on the operator
                if token == "+":
                    # Pop the last two numbers, add them, and push the result back
                    number_stack[-2] += number_stack[-1]
                elif token == "-":
                    # Pop the last two numbers, subtract the second from the first, and push back
                    number_stack[-2] -= number_stack[-1]
                elif token == "*":
                    # Pop the last two numbers, multiply, and push the result back
                    number_stack[-2] *= number_stack[-1]
                else: # Division
                    # Ensure integer division for negative numbers too
                    number_stack[-2] = int(float(number_stack[-2]) / number_stack[-1])
                # Pop the last number (second operand) from the stack as it's been used
                number_stack.pop()
      
        # Return the result which is the only number left in the stack
        return number_stack[0]
