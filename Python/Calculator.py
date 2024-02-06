# Write a program to calculate the result of an expression

operators = [['*','/'],['+','-']]

class Stack:

  maxSize = 100
  items = [None] * maxSize
  stackPointer = -1


class StackOverFlowException(Exception):
  pass


class StackUnderFlowException(Exception):
  pass


def is_full(s):
  return s.stackPointer == s.maxSize - 1


def is_empty(s):
  return s.stackPointer == -1


def push(item, s):
  if not is_full(s):
    s.stackPointer += 1
    s.items[s.stackPointer] = item
  else:
    raise StackOverFlowException


def pop(s):
  if not is_empty(s):
    s.stackPointer -= 1
    return s.items[s.stackPointer + 1]
  else:
    raise StackUnderFlowException


def peek(s):
  if not is_empty(s):
    return s.items[s.stackPointer]
  else:
    raise StackUnderFlowException

def dump(s):
  i = s.stackPointer
  while i >= 0:
    print(s.items[i])
    i -= 1

def getLength(s):
  return s.stackPointer+1


def isOperator(c):
  if c in operators[0] or c in operators[1]:
    return True
  return False

def higherPreced(op1,op2):
  if op1 in operators[0] and op2 in operators[1]:
    return True
  elif (op1 in operators[0] and op2 in operators[0]) or (op1 in operators[1] and op2 in operators[1]):
    return True
  return False

def performOperation(op1,op2,operator):
  if operator == "+":
    return op1 + op2
  elif operator == "-":
    return op1 - op2
  elif operator == "*":
    return op1 * op2
  else:
    return op1 / op2


def RPS(exp):
  s = Stack()
  res = ""
  for i in range(0,len(exp)):
    if not isOperator(exp[i]):
      res += exp[i]
    else:
      while not is_empty(s) and higherPreced(peek(s),exp[i]):
        res += pop(s)
      push(exp[i],s)

  while not is_empty(s):
    res += pop(s)
  return res

def evaluate(exp):
    s = Stack()
    for i in range(0,len(exp)):
      if not isOperator(exp[i]):
        push(exp[i],s)
      else:
        op2 = float(pop(s))
        op1 = float(pop(s))
        temp = performOperation(op1,op2,exp[i])
        push(str(temp),s)

    return peek(s)
        


print(evaluate(RPS("5*3-4/3/2+3+9*6")))       