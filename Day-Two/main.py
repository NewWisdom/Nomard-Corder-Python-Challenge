"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""
def is_on_list(days,day):
  if type(days) == list and type(day) == str:
    if day in days:
      return True
  return False

def get_x(days,num):
  return days[num]

def add_x(days,day):
  if type(days) ==list and type(day) == str:
    days.append(day) 

def remove_x(days,day):
  if type(days) == list and type(day) == str:
    days.remove(day)
# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #



