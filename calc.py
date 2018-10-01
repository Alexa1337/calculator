# calculator
#calculator
import math
def suma(a,b):
    return a + b

def raz(a,b):
    return a - b

def div(a,b):
    count = 0
    while a >= b:
        a -= b
        count += 1
    return count

def mul(a,b):
    count = 0
    while b > 0:
        b = b - 1
        count += a
    return count

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def ost(a,b):
    return a % b

def sqr(a,b):
    result = 1
    while b > 0:
        b -= 1
        result *= a
    return result

print("Enter a first number")
x = int(input())
#int(input())
print('Yet ?')
answer = str(input())
if answer =='Yes':
    print("Enter a secind number")
    y = int(input())
    print('What action do you want to take?')
    act = str(input())
    if act ==  '+' :
        print(x, '+', y,'=',suma(x,y))
    
    elif act == '-':
        print(x, '+',y,'=',raz(x,y))
    
    elif act == '-':
        print(x, '-', y,'=',raz(x,y))
    
    elif act == '*':
        print(x, '*', y,'=',mul(x,y))
    
    elif act == '/':
        print(x, '/', y,'=',div(x,y))
    
    elif act == '%':
        print(x, '%', y,'=',ost(x,y))
    
    elif act == '**':
        print(x, '**', y,'=',sqr(x,y))
elif answer == 'No':
    print('What action do you want to take?')
    act = str(input())
    if act == '!':
        print('!', fact(x))


