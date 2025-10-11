import time
import sys

class Calculator:
    def __init__(self, num1, num2, action):
        self.num1 = num1; self.num2 = num2; self.action = action
    def valueCheck(self):
        num_list = [str(self.num1), str(self.num2)]
        act_list = ['+', '-', '*', '/']
        for number in  num_list:
            for digit in number:
                if ord('0') > ord(digit) or ord(digit) > ord('9'):
                    raise ValueError(f'The given number is invalid: {number}')
        if self.action not in act_list:
            raise ValueError(f'The given action is invalid: {self.action}')
    def add(self):
        return self.num1 + self.num2
    def subtr(self):
        return self.num1 - self.num2
    def mult(self):
        return self.num1 * self.num2
    def div(self):
        if self.num2 == 0:
            raise ZeroDivisionError('Division by zero')
        else:
            return self.num1 / self.num2
    def goofyStyl(self):
        for i in range(14):
            if i != 13:
                print('~', end='')
            else:
                print('~')
def main():
    try:
        if len(sys.argv) == 4:
            num1 = int(sys.argv[1])
            num2 = int(sys.argv[3])
            action = sys.argv[2]

            calc = Calculator(num1, num2, action)
            calc.valueCheck()
            result = 0
            if action == '+':
                result = calc.add()
            elif action == '-':
                result =  calc.subtr()
            elif action == '*':
                result = calc.mult()
            elif action == '/':
                result = calc.div()
            print('\nCalculating...')
            time.sleep(3)
            print('Finished.\n')
            time.sleep(1)
            calc.goofyStyl()
            print(f'The result: {result}')
            calc.goofyStyl()
        else:
            raise ValueError('Unsupported number of arguments: Expected 4 (including filename')
    except Exception as error:
        print(f'Unexpected error occured: {error}')
if __name__=='__main__':
    main()
