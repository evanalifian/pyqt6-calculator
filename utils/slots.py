from PyQt6.QtWidgets import QLineEdit
from dsa import Stack, evaluate_infix


def formatNumber(value: float):
  # 4.0 ditampilkan sebagai 4, sisanya dibatasi 10 angka signifikan
  if float(value).is_integer():
    return str(int(value))
  return f"{value:.10g}"


def readNumber(lineEdit: QLineEdit):
  # Ambil isi line edit sebagai angka, tampilkan pesan jika tidak valid
  try:
    return float(lineEdit.text().replace(",", ".").strip())
  except ValueError:
    lineEdit.setText("Error: masukkan angka dulu")
    return None


def pushMathStack(title: str, lineEdit: QLineEdit, mathStack: Stack):
  mathStack.push(title)
  lineEdit.insert(str(title))


def calculate(mathStack: Stack, lineEdit: QLineEdit = None):
  # Ekspresi diambil dari line edit supaya hasil operasi lain (x², 1/x, √x)
  # atau ketikan manual tetap ikut terhitung
  if lineEdit is not None:
    expression = lineEdit.text()
  else:
    expression = "".join(mathStack.stack)

  try:
    result = evaluate_infix(expression)
    if lineEdit is not None:
      lineEdit.setText(formatNumber(result))
    else:
      print(formatNumber(result))
  except Exception as exc:
    if lineEdit is not None:
      lineEdit.setText(f"Error: {exc}")
    else:
      print(f"Error: {exc}")

  mathStack.stack.clear()

def squared(lineEdit: QLineEdit):
  num = readNumber(lineEdit)
  if num is None:
    return

  lineEdit.setText(formatNumber(num ** 2))

def multiplicativeInverse(lineEdit: QLineEdit):
  num = readNumber(lineEdit)
  if num is None:
    return

  if num == 0:
    lineEdit.setText("Error: tidak bisa dibagi nol")
    return

  lineEdit.setText(formatNumber(1 / num))

def squareRoot(lineEdit: QLineEdit):
  num = readNumber(lineEdit)
  if num is None:
    return

  if num < 0:
    lineEdit.setText("Error: bilangan negatif tidak memiliki akar real")
    return
  if num == 0:
    lineEdit.setText("0")
    return

  # Metode Newton
  guess = num

  for i in range(100):
    newGuess = (guess + num / guess) / 2

    if abs(newGuess - guess) < 0.000001:
      guess = newGuess
      break

    guess = newGuess

  lineEdit.setText(formatNumber(guess))
