email = input("Enter your email: ")
k,j,d= 0,0,0
if len(email)>= 6 :#1
  if email[0].isalpha():#2
    if ("@"in email) and (email.count("@")==1):#2
      if ((email[-3]==".") or (email[-4]==".")):#4
        for  i in email: #5
          if i==i.isspace():
            k=1
          elif i.isalpha() :
            if i==i.upper():
              j=1
          elif i.isdigit():
            continue
          elif i=="_" or i=="." or i=="@":
            continue
          else:
            d=1
        if k==1 or j==1 or d==1:
          print("Invalid email 5")
      else:
        print("Invalid email format 4.")
    else :
      print("Invalid email format 3.")
  else:
    print("Email should start with a letter 2.")
else:
  print("Email should have at least 6 characters 1.")
  