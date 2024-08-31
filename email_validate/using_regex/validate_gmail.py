#a-z   alister@gmail.com
#0-9
# . _  @ only 1 time per email
# . at email[-3(.in) or  -4(.com)]

import re #regex module import

#"^ for ranging" and "\ for searching using regex" and "$ for searching from behind"
email_conditions = "^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"  #optimal email conditions

# Enhanced email regex conditions
email_conditions2 = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


user_email = input("Please enter your email address: ")

if re.search(email_conditions, user_email):
  print("Valid email address for optimal!")
else:
  print("Invalid email address for optimal.")

if re.search(email_conditions2, user_email):
  print("Valid email address for enhanced!")
else:
  print("Invalid email address for enhanced.")