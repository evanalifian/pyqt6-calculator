class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)


def normalize_expression(expression: str):
  return expression.replace("×", "*").replace("÷", "/").strip()


def is_number(token: str):
  try:
    float(token)
    return True
  except ValueError:
    return False


def is_operator(token: str):
  return token in {"+", "-", "*", "/", "%", "^"}


def precedence(operator: str):
  if operator in {"+", "-"}:
    return 1
  if operator in {"*", "/", "%"}:
    return 2
  if operator == "^":
    return 3
  return 0


def tokenize_expression(expression: str):
  expr = normalize_expression(expression)
  if expr == "":
    return []

  tokens = []
  current = ""

  for char in expr:
    if char.isspace():
      if current:
        tokens.append(current)
        current = ""
      continue

    if char.isdigit() or char == ".":
      current += char
    elif char in "+-*/%^()":
      if current:
        tokens.append(current)
        current = ""
      tokens.append(char)
    else:
      raise ValueError(f"Invalid character: {char}")

  if current:
    tokens.append(current)

  return tokens


def infix_to_postfix(expression: str):
  tokens = tokenize_expression(expression)
  output = []
  operators = Stack()

  for token in tokens:
    if is_number(token):
      output.append(token)
    elif token == "(":
      operators.push(token)
    elif token == ")":
      while not operators.isEmpty() and operators.peek() != "(":
        output.append(operators.pop())
      if operators.isEmpty():
        raise ValueError("Invalid expression: missing '('")
      operators.pop()
    elif is_operator(token):
      while (
        not operators.isEmpty()
        and operators.peek() != "("
        and precedence(operators.peek()) >= precedence(token)
      ):
        output.append(operators.pop())
      operators.push(token)

  while not operators.isEmpty():
    if operators.peek() == "(":
      raise ValueError("Invalid expression: missing ')' ")
    output.append(operators.pop())

  return " ".join(output)


def infix_to_prefix(expression: str):
  tokens = tokenize_expression(expression)
  reversed_tokens = []
  for token in reversed(tokens):
    if token == "(":
      reversed_tokens.append(")")
    elif token == ")":
      reversed_tokens.append("(")
    else:
      reversed_tokens.append(token)

  postfix = infix_to_postfix(" ".join(reversed_tokens))
  return " ".join(reversed(postfix.split()))


def evaluate_postfix(postfix_expression: str):
  tokens = tokenize_expression(postfix_expression)
  values = Stack()

  for token in tokens:
    if is_number(token):
      values.push(float(token))
    elif is_operator(token):
      if values.size() < 2:
        raise ValueError(f"Invalid postfix expression: {postfix_expression}")

      right = values.pop()
      left = values.pop()

      if token == "+":
        result = left + right
      elif token == "-":
        result = left - right
      elif token == "*":
        result = left * right
      elif token == "/":
        if right == 0:
          raise ZeroDivisionError("Division by zero is not allowed")
        result = left / right
      elif token == "%":
        if right == 0:
          raise ZeroDivisionError("Modulo by zero is not allowed")
        result = left % right
      elif token == "^":
        result = left ** right
      else:
        raise ValueError(f"Unsupported operator: {token}")

      values.push(result)
    else:
      raise ValueError(f"Invalid token in postfix expression: {token}")

  if values.size() != 1:
    raise ValueError("Invalid postfix expression")

  result = values.pop()
  return result


def evaluate_prefix(prefix_expression: str):
  tokens = tokenize_expression(prefix_expression)
  stack = Stack()

  for token in reversed(tokens):
    if is_number(token):
      stack.push(float(token))
    elif is_operator(token):
      if stack.size() < 2:
        raise ValueError(f"Invalid prefix expression: {prefix_expression}")

      left = stack.pop()
      right = stack.pop()

      if token == "+":
        stack.push(left + right)
      elif token == "-":
        stack.push(left - right)
      elif token == "*":
        stack.push(left * right)
      elif token == "/":
        if right == 0:
          raise ZeroDivisionError("Division by zero is not allowed")
        stack.push(left / right)
      elif token == "%":
        if right == 0:
          raise ZeroDivisionError("Modulo by zero is not allowed")
        stack.push(left % right)
      elif token == "^":
        stack.push(left ** right)
      else:
        raise ValueError(f"Unsupported operator: {token}")
    else:
      raise ValueError(f"Invalid token in prefix expression: {token}")

  if stack.size() != 1:
    raise ValueError("Invalid prefix expression")

  return stack.pop()


def evaluate_infix(infix_expression: str):
  postfix_expression = infix_to_postfix(infix_expression)
  return evaluate_postfix(postfix_expression)