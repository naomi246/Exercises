# performance task problem 2 - Do the shuffle
import random

class RangeError(Exception):
  pass

class PressRangeError(Exception):
  pass

icsmp = ["A", "B", "C", "D", "E"]
end = -1
def button_1(x):
  for i in range(presses):
    first = icsmp[0]
    icsmp.append(icsmp.pop(icsmp.index(first)))
  print(icsmp)

def button_2(x):
  for i in range(presses):
    last = icsmp[4]
    icsmp.insert(0,icsmp.pop(icsmp.index(last)))
  print(icsmp)

def button_3(x):
  for i in range(presses):
    icsmp[0], icsmp[1] = icsmp[1], icsmp[0]
  print(icsmp)

def button_4(p):
  num = random.randint(1,3)
  if num == 1:
    print("Random choice is button 1.")
    button_1(p)
  elif num == 2:
    print("Random choice is button 2.")
    button_2(p)
  elif num == 3:
    print("Random choice is button 3.")
    button_3(p)

  

  

for i in range(10):
  while True: 
    try: 
      button = int(input("Button number: "))
      if button <= 0 or button > 5:
        raise RangeError
      presses = int(input("Presses: "))
      if presses <= 0 or presses > 10:
        raise PressRangeError
      break
  
    except RangeError: 
      print("Please select a button between 1 and 4")

    except PressRangeError:
      print("Please select a number of presses from 1-10")
  
    except ValueError: 
      print("Invalid entry - Please enter an integer")
  
  if button == 1:
    #moves first song to end of playlist
    button_1(presses)
  
  elif button == 2: 
    #moves last song to start of playlist
    button_2(presses)
  
  elif button == 3: 
    #swaps first two songs in playlist
    button_3(presses)

  elif button == 4:
    #randmoly chooses remix method
    num = random.randint(1,3)
    button_4(presses)
  
  elif button == 5:
    #quits program
    print("The final order of your playlist is:", icsmp)
    end = 1
    break   

if end == -1:
  print("You have reached the limit of entries.")
  print("The final order of your playlist is:", icsmp)


  



  
