#performance task problem 1

class HumidityRangeError(Exception):
  pass

class TimeRangeError(Exception):
  pass

def balloon_height(h,t):
  for i in range(t):
    i += 1
    A = -6*i**4 + h*i**3 + 2*i**2 + i
    if A <= 0: 
      return i
      
while True: 
  try: 
    h_factor = int(input("Enter the humidity factor (0-100): "))
    if h_factor < 0 or h_factor > 100:
      raise HumidityRangeError
    
    time = int(input("Enter the maximum number of hours you will wait (0-24): "))
    if time < 0 or time > 24:
      raise TimeRangeError

    break

  except ValueError:
    print("Please enter an integer.")

  except HumidityRangeError: 
    print("The humidity factor must between 0 - 100.")

  except TimeRangeError:
    print("The time must be between 0 - 24 hours.")

x = balloon_height(h_factor, time)

if x == None:
  print("The balloon will not hit the ground within the specified time.")

else: 
  print("The balloon will hit the ground after",x,"hour/s.")

  



    
    
