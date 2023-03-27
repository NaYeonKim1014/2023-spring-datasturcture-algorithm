def evaluate_postfix(lst):
    op_check = ['+','/','*','-']    # Pre-generated for operator check
    stack =[]   # Create a list to add operands 
    a1=0   # Creating variables for stack[-1]
    a2=0  # Creating variables for stack[-2]
    for l in range(len(lst)):   # Repeat as many lists as are stored as postfix expressions
        if lst[l].isdigit():    # If it is an operand, add it to the stack immediately
            stack.append(int(lst[l]))
        elif lst[l] == '+': # If it's '+', pop two operands from the stack and calculate and add them back to the stack
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 + a2)
        elif lst[l] == '-': # If it's '-', pop two operands from the stack and calculate and add them back to the stack
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 - a2) 
        elif lst[l] == '*': # If it's '*', pop two operands from the stack and calculate and add them back to the stack
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 * a2)
        elif lst[l] == '/': # If it's '/', pop two operands from the stack and calculate and add them back to the stack
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 / a2)
    return stack[0]

lst = input("Input postfix expression :")
result = evaluate_postfix(lst)
print("Result is",result)
