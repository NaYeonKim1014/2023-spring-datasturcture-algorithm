class Gate:
    def evaluate(self, assignments):
        pass

class AndGate(Gate):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, assignments):
        return self.left.evaluate(assignments) and self.right.evaluate(assignments)

class OrGate(Gate):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, assignments):
        return self.left.evaluate(assignments) or self.right.evaluate(assignments)

class NotGate(Gate):
    def __init__(self, operand):
        self.operand = operand

    def evaluate(self, assignments):
        return not self.operand.evaluate(assignments)

class Variable(Gate):
    def __init__(self, name):
        self.name = name

    def evaluate(self, assignments):
        return assignments[self.name]

def parse_expression(expr):
    # 식 파싱하여 논리 게이트를 만들기
    tokens = expr.split()
    stack = []
    for token in tokens:
        if token == "A":
            right = stack.pop()
            left = stack.pop()
            stack.append(AndGate(left, right))
        elif token == "V":
            right = stack.pop()
            left = stack.pop()
            stack.append(OrGate(left, right))
        elif token == "-":
            operand = stack.pop()
            stack.append(NotGate(operand))
        else:
            stack.append(Variable(token))
    return stack.pop()

def dpll(expression, variables, assignments={}):
    # DPLL 알고리즘을 사용하여 식을 True로 만들 수 있는지 확인
    if isinstance(expression, (AndGate, OrGate)):
        # 논리 게이트의 왼쪽과 오른쪽 피연산자에 대한 재귀 호출 수행
        left = expression.left
        right = expression.right
        left_result = dpll(left, variables, assignments)
        right_result = dpll(right, variables, assignments)
        if left_result is None or right_result is None:
            return None
        if isinstance(expression, AndGate):
            return left_result and right_result
        else:
            return left_result or right_result
    elif isinstance(expression, NotGate):
        # NotGate의 피연산자에 대한 재귀 호출 수행
        operand = expression.operand
        operand_result = dpll(operand, variables, assignments)
        if operand_result is None:
            return None
        return not operand_result
    elif isinstance(expression, Variable):
        # 변수에 값을 할당하고 해당 식이 True로 평가되는지 확인
        variable_name = expression.name
        if variable_name in assignments:
            # 변수에 이미 값을 할당했음
            return assignments[variable_name]
        for value in [True, False]:
            # 변수에 값을 할당
            new_assignments = assignments.copy()
            new_assignments[variable_name] = value
            # 남은 변수에 대한 재귀 호출 수행
            remaining_variables = [v for v in variables if v not in new_assignments]
            if len(remaining_variables) == 0:
                # 모든 변수에 값 할당함
                if expression.evaluate(new_assignments):
                    # 식이 True로 평가됨
                    return True
            else:
                result = dpll(expression, remaining_variables, new_assignments)
                if result is not None and result:
                    # 식이 True로 평가됨
                    return True
        # 식이 False로 평가됨
        return False

expression = parse_expression("(x1 - x2) V (-x1 A x3) V -x3")
variables = ["x1", "x2", "x3"]
result = dpll(expression, variables)
print(result)
