from PyQt6.QtWidgets import QLineEdit
from dsa import Stack, evaluate_infix


def pushMathStack(title: str, lineEdit: QLineEdit, mathStack: Stack):
  mathStack.push(title)
  lineEdit.insert(str(title))


def calculate(mathStack: Stack, lineEdit: QLineEdit = None):
  expression = "".join(mathStack.stack)

  try:
    result = evaluate_infix(expression)
    if lineEdit is not None:
      lineEdit.setText(str(result))
    else:
      print(result)
  except Exception as exc:
    if lineEdit is not None:
      lineEdit.setText(f"Error: {exc}")
    else:
      print(f"Error: {exc}")

  mathStack.stack.clear()