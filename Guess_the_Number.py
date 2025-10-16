from random import randint
import time

class Random_Num:
  def __init__(self, name, number, secret_num):
    self.name = name
    self.number = number
    self.secret_num = secret_num
  def input_check(self):
    str_list =list(self.number)
    for index, char in enumerate(str_list):
      if (index != 0) and (char == '-'):
        return'🔴Please, enter a valid number:\n   '
      elif index == 0 and char == '-':
        continue
      elif ord(char) < ord('0') or ord(char) > ord('9'):
        return '🔴Please, enter a valid number:\n   '
    if int(self.number) > 100 or int(self.number) < 0:
        return '🔴The number should be in the range of 1-100:\n   '
    return None
  def analyzer(self):
    check_result = self.input_check()
    if check_result != None:
      return check_result
    self.number = int(self.number)
    if self.number > self.secret_num:
      return 'Smaller 📉:\n   '
    elif self.number < self.secret_num:
      return 'Bigger 📈:\n   '
    else:
      return 'Gotcha'

def main():
  secret_num = randint(1,100)
  usr = Random_Num('', '', secret_num)
  usr.name = input('Before starting, please enter your name: ')
  print(f'Hello {usr.name} 🙂! Welcome to the game "Guess the Number".')
  time.sleep(3)
  print('🎉 Rules: Guess the secret number between 1 and 100!')
  time.sleep(2)
  print("Remember☝️, you have got only 6 hearts ❤️!")
  time.sleep(4)
  print("Ready?")
  time.sleep(2)
  print("Let's go!")
  time.sleep(1)
  print('Choosing a random number... 🤔')
  time.sleep(4)
  counter = 0
  hearts = 6
  result = ''
  while usr.number != usr.secret_num:
    if counter == 0:
      usr.number = input("Now, guess the number between 1 to 100:\n   ")
    result = usr.analyzer()
    if usr.number != usr.secret_num:
      usr.number = input(f'{result} ')
      if '🔴' not in result:
        hearts -= 1
    else:
      break
    if hearts == 0:
      print('Sorry, you ran out of hearts 💔')
      time.sleep(2)
      print('Game Over.\n')
      break
    counter += 1
  if result == 'Gotcha':
    print(f'Gotcha 😊! You found the secret number {usr.secret_num}!\n')
  time.sleep(3)
  print('Stay tuned for upcoming releases 💀')
  
if __name__=='__main__':
  main()
  
  