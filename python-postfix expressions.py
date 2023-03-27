def evaluate_postfix(lst):
    op_check = ['+','/','*','-']    # 연산자 체크를 위해 미리 생성
    stack =[]   # 피연산자 바로 추가할 리스트 생성
    a1=0   # stack[-1]을 위한 변수 생성
    a2=0  # stack[-2]을 위한 변수 생성
    for l in range(len(lst)):   # 후위표기법으로 저장되 있는 리스트의 수만큼 반복   
        if lst[l].isdigit():    # 만약 피연산자이면 바로 stack에 추가
            stack.append(int(lst[l]))
        elif lst[l] == '+': # + 이면 stack에서 2개 피연산자를 pop하여 게산해준뒤 다시 stack에 추가
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 + a2)
        elif lst[l] == '-': # - 이면 stack에서 2개 피연산자를 pop하여 게산해준뒤 다시 stack에 추가
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 - a2) 
        elif lst[l] == '*': # * 이면 stack에서 2개 피연산자를 pop하여 게산해준뒤 다시 stack에 추가
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 * a2)
        elif lst[l] == '/': # / 이면 stack에서 2개 피연산자를 pop하여 게산해준뒤 다시 stack에 추가
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a1 / a2)
    return stack[0]

lst = input("후위 표기식을 입력하세요 :")
result = evaluate_postfix(lst)
print("결과는",result)
