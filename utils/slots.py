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

def squared(num: int, lineEdit: QLineEdit):
  formula = num ** 2
  lineEdit.setText(str(formula))

def multiplicativeInverse(num: int, lineEdit: QLineEdit):
  formula = 1 / num
  lineEdit.setText(str(formula))

def squareRoot(num: int, lineEdit: QLineEdit):
  if num < 0:
    lineEdit.setText("Bilangan negatif tidak memiliki akar real")
  if num == 0:
    lineEdit.setText("0")

  guess = num

  for i in range(100):
    newGuess = (guess + num / guess) / 2

    if abs(newGuess - guess) < 0.000001:
      lineEdit.setText(str(newGuess))

    guess = newGuess

  lineEdit.setText(str(guess))